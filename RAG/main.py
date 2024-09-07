import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

if __name__ == "__main__":
    llm = ChatGroq(
        temperature=0,
        model="llama-3.1-70b-versatile",
        groq_api_key=GROQ_API_KEY
    )

    prompt = "How to find the right mortgage in Canada?"
    response = llm.invoke(prompt)
    print('LLM Response: \n', response.content)
