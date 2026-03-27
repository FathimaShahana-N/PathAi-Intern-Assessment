from fastapi import FastAPI
from api.routes.ask import router

app = FastAPI(
    title="PathAI Career Guidance API",
    description="A FastAPI backend that uses Groq LLM to answer student career queries.",
    version="1.0.0",
)

app.include_router(router)