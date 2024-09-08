import streamlit as st
from chains import Chain
from portfolio import Portfolio
from utils import clean_text
from langchain_community.document_loaders import WebBaseLoader


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("Cold Email Generator")

    JOB_URL = {
        "NLP": "https://presto.applytojob.com/apply/job_20231227212946_OPCANGUTNYCRGJ0X",
        "DATA_SCIENTISTS": "https://presto.applytojob.com/apply/job_20240702173546_K6ZLCUHZTSRZZS6Y",
        "ASR": "https://presto.applytojob.com/apply/job_20240825210440_ULSLZVY8SVSRULJP",
        "INTERN": "https://presto.applytojob.com/apply/job_20240625192645_O6OHJW7GQDL35TVZ"
    }
    option = st.selectbox(
        "Choose the Job URL",
        options=list(JOB_URL.keys())
    )

    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([JOB_URL[option]])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)