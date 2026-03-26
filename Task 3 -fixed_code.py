from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str

@app.post('/ask', response_model=QueryResponse)
async def ask(request: QueryRequest):
    result = await call_llm(request.query)
    return QueryResponse(response=result)

async def call_llm(query: str) -> str:
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            'https://api.example-llm.com/generate',
            json={'prompt': query},
            timeout=30.0
        )
        data = resp.json()
        return data['output']
