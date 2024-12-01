from fastapi import FastAPI
from inference import RAGQuery
from pydantic import BaseModel

class Item(BaseModel):
    query: str

app = FastAPI()
PERSIST_PATH = "./chroma"
ragquery = RAGQuery(PERSIST_PATH)

@app.post("/")
async def query(query:Item):
    response = ragquery.query(query.query)
    return response
