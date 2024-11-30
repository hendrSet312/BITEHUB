from fastapi import FastAPI
#from inference import RAGQuery

app = FastAPI()

@app.post("/")
async def query(query:str):
    return query
