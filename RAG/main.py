import os
# import chromadb
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


class RetrievalAugmentedGeneration:
    # vector_db_client = chromadb.Client()

    def __init__(self, temperature: int = 0, ):
        load_dotenv()
        self.llm = ChatGroq(
            temperature=temperature,
            model="llama-3.1-70b-versatile",
            groq_api_key=os.environ.get("GROQ_API_KEY", "")
        )
        # self.vector_db_collection = self.vector_db_client.create_collection(name="serhan_vector_db_collection")
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
            'write_email': None
        }
        self.langchain_extract_page_content = self.prompt['extract_page_content'] | self.llm
        self.json_parser = JsonOutputParser()

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
        resp = self.langchain_extract_page_content.invoke(input=dict(page_data=page_data))

        if resp.content:
            output = self.json_parser.parse(resp.content)
        return output


if __name__ == "__main__":
    rag = RetrievalAugmentedGeneration()
    # response = rag.ask_llm("How to find halal mortgage in Canada?")
    # print('LLM Response: \n', response.content)

    URL = {
        "NLP": "https://presto.applytojob.com/apply/job_20231227212946_OPCANGUTNYCRGJ0X",
        "DATA_SCIENTISTS": "https://presto.applytojob.com/apply/job_20240702173546_K6ZLCUHZTSRZZS6Y"
    }
    print('LLM JSON Response: \n', rag.get_web_page_content(URL["DATA_SCIENTISTS"]))
