import numpy
import os
import chromadb
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
import keras
import keras_hub
import kagglehub

kagglehub.login()

PERSIST_PATH = './chroma'

class RAGQuery:
    
    def __init__(self, persist_path):
        self.PERSIST_PATH = persist_path
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
        print("Initializing vector store")
        self.food_vector_store = Chroma(collection_name="food_calories", persist_directory=self.PERSIST_PATH, embedding_function=self.embeddings)
        print("importing model")
        self.gemma_lm = keras_hub.models.GemmaCausalLM.from_preset("gemma2_instruct_2b_en")

    def query(self, user_query):
        search_result = self.food_vector_store.similarity_search(query=user_query, k=3)
        context = "\n".join([f"{doc.page_content}" for doc in search_result])
        prompt = f"Context: {context}\n\nQuestion: {user_query}\n\nAnswer:"
        response = self.gemma_lm.generate(prompt)
        return response







