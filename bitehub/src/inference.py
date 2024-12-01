import numpy
import os
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import chromadb
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
import requests


PERSIST_PATH = './chroma/'
API_KEY = 'AIzaSyDpAbVqqklGM65cKu22CaCF_1hizBSWt88'

class RAGQuery:
    
    def __init__(self, persist_path):
        self.PERSIST_PATH = persist_path
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        print("Initializing vector store")
        self.food_vector_store = Chroma(collection_name="food_calories", persist_directory=self.PERSIST_PATH, embedding_function=self.embeddings)

    def query(self, user_query):
        search_result = self.food_vector_store.similarity_search(query=user_query, k=3)
        context = "\n".join([f"{doc.page_content}" for doc in search_result])
        prompt = f"Context: {context}\n\nQuestion: {user_query}\n\nAnswer:"
        headers = {'Content-Type': 'application/json',}
        params = {'key': API_KEY,}
        json_data = {
            'contents': [
                {
                    'parts': [
                        {
                            'text': prompt,
                        },
                    ],
                },
            ],
        }


        response = requests.post(
            'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent',
            params=params,
            headers=headers,
            json=json_data,
        )
        
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]







