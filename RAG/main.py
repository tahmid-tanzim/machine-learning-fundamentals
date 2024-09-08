import os
import uuid
import chromadb
import pandas as pd
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

dir_path = os.path.dirname(os.path.realpath(__file__))


class RetrievalAugmentedGeneration:
    vector_db_client = chromadb.PersistentClient(f'{dir_path}/vector_db')

    def __init__(self, temperature: int = 0, ):
        load_dotenv()
        self.llm = ChatGroq(
            temperature=temperature,
            model="llama-3.1-70b-versatile",
            groq_api_key=os.environ.get("GROQ_API_KEY", "")
        )
        self.prompt = {
            'extract_page_content': PromptTemplate.from_template(
                """
                ### SCRAPED TEXT FROM WEBSITE:
                {page_data}
                ### INSTRUCTION:
                The scraped text is from the career's page of a website. 
                Your job is to extract the job postings and return them in JSON format containing
                following keys: `role`, `experience`, `skills` and `description`.
                Only return the valid JSON.
                ### VALID JSON (NO PREAMBLE):
                """
            ),
            'write_email': PromptTemplate.from_template(
                """
                ### JOB DESCRIPTION:
                {job_description}
                ### INSTRUCTION:
                You are Serhan, a business development executive at AtliQ. 
                AtliQ is an AI & Software Consulting company dedicated to facilitating
                the seamless integration of business processes through automated tools. 
                Over our experience, we have empowered numerous enterprises with tailored solutions, 
                fostering scalability, process optimization, cost reduction, and heightened overall efficiency. 
                Your job is to write a cold email to the client regarding the job mentioned above 
                describing the capability of AtliQ in fulfilling their needs.
                Also add the most relevant ones from the following links to showcase Atliq's portfolio: {url_list}
                Remember you are Serhan, BDE at AtliQ. 
                Do not provide a preamble.
                ### EMAIL (NO PREAMBLE):
                """
            ),
        }
        self.json_parser = JsonOutputParser()
        self.vector_db_collection = self.vector_db_client.get_or_create_collection(name="company_portfolio_collection")
        self.init_vector_db()

    def init_vector_db(self):
        if not self.vector_db_collection.count():
            portfolio_dataframe = pd.read_csv(f"{dir_path}/company_portfolio.csv")
            for _, row in portfolio_dataframe.iterrows():
                self.vector_db_collection.add(
                    documents=row["Tech Stack"],
                    metadatas=dict(links=row["URLs"]),
                    ids=[str(uuid.uuid4())]
                )

    def ask_llm(self, prompt: str):
        if not prompt:
            return
        return self.llm.invoke(prompt)

    def get_web_page_content(self, url: str) -> dict:
        output = dict()
        if not url:
            return output

        loader = WebBaseLoader(url)
        page_data = loader.load().pop().page_content

        # Chaining Prompt & LLM
        langchain_extract_page_content = self.prompt['extract_page_content'] | self.llm
        resp = langchain_extract_page_content.invoke(input=dict(page_data=page_data))

        if resp.content:
            output = self.json_parser.parse(resp.content)
        return output

    def semantic_search(self, skills):
        return self.vector_db_collection.query(
            query_texts=skills,
            n_results=2
        ).get('metadatas', [])

    def write_email(self, job):
        url_list = self.semantic_search(job["skills"])

        # Chaining Prompt & LLM
        langchain_write_email = self.prompt['write_email'] | self.llm
        resp = langchain_write_email.invoke(input=dict(job_description=str(job), url_list=url_list))
        return resp.content or ""


if __name__ == "__main__":
    rag = RetrievalAugmentedGeneration()

    # response = rag.ask_llm("How to find halal mortgage in Canada?")
    # print('LLM Response: \n', response.content)

    URL = {
        "NLP": "https://presto.applytojob.com/apply/job_20231227212946_OPCANGUTNYCRGJ0X",
        "DATA_SCIENTISTS": "https://presto.applytojob.com/apply/job_20240702173546_K6ZLCUHZTSRZZS6Y",
        "ASR": "https://presto.applytojob.com/apply/job_20240825210440_ULSLZVY8SVSRULJP",
        "INTERN": "https://presto.applytojob.com/apply/job_20240625192645_O6OHJW7GQDL35TVZ"
    }
    extracted_job = rag.get_web_page_content(URL["ASR"])
    print('Extracted Job Response: \n', extracted_job)
    print('\nEmail for the Job: \n', rag.write_email(extracted_job))
