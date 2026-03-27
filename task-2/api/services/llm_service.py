import os
import time
import httpx
from dotenv import load_dotenv
from typing import Tuple

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama-3.1-8b-instant"

SYSTEM_PROMPT = (
    "You are a helpful career guidance assistant for students in Kerala, India "
    "who have just finished their 12th board exams. You give clear, specific, and "
    "honest career advice based on the student's situation. Keep responses concise "
    "and easy to understand."
)


async def call_llm(query: str) -> Tuple[str, float]:
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set in environment variables")

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query},
        ],
        "max_tokens": 512,
    }

    start_time = time.time()

    async with httpx.AsyncClient() as client:
        resp = await client.post(
            GROQ_API_URL,
            headers=headers,
            json=payload,
            timeout=30.0,
        )
        resp.raise_for_status()

    latency_ms = (time.time() - start_time) * 1000
    data = resp.json()
    response_text = data["choices"][0]["message"]["content"]

    return response_text, latency_ms