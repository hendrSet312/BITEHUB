from fastapi import FastAPI
from inference import RAGQuery

app = FastAPI()
PERSIST_PATH = "./chroma"

@app.post("/")
async def query(query:str):
    ragquery = RAGQuery(PERSIST_PATH)
    response = ragquery.query("How much calories are in beetroot?")
    return response
