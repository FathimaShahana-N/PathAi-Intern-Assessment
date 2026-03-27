from pydantic import BaseModel


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    response: str
    model: str
    latency_ms: float


class ErrorResponse(BaseModel):
    error: str