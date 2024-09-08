import os
import pandas as pd
import chromadb
import uuid


class Portfolio:
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.data = pd.read_csv(f"{dir_path}/resource/company_portfolio.csv")
        self.chroma_client = chromadb.PersistentClient(f"{dir_path}/vectorstore")
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["Tech Stack"],
                                    metadatas={"links": row["URLs"]},
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])