# Task 2 — PathAI Career Guidance API

A FastAPI backend that accepts student career queries and returns AI-generated responses using the Groq API (Llama 3).

## Why Groq?
Groq offers a free tier with very fast inference speeds and supports Llama 3, making it ideal for a low-latency career guidance assistant.

## Project Structure
```
task-2/
├── main.py               # App entry point
├── requirements.txt      # Dependencies
├── .env.example          # Environment variable template
├── README.md
└── api/
    ├── routes/
    │   └── ask.py        # /ask and /health endpoints
    ├── models/
    │   └── schemas.py    # Pydantic request/response models
    └── services/
        └── llm_service.py  # Groq API call logic
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/FathimaShahana-N/PathAi-Intern-Assessment.git
cd PathAi-Intern-Assessment/task-2
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
```bash
cp .env.example .env
```
Open `.env` and add your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get a free API key at [groq.com](https://groq.com)

### 4. Run the server
```bash
uvicorn main:app --reload
```

The API will be running at `http://localhost:8000`

## API Endpoints

### POST /ask
Accepts a student query and returns an AI-generated career guidance response.

**Request:**
```json
{
  "query": "I scored 85% in PCM. Should I choose engineering or medicine?"
}
```

**Response:**
```json
{
  "response": "Based on your score...",
  "model": "llama3-8b-8192",
  "latency_ms": 523.12
}
```

### GET /health
Returns server status and model name.

**Response:**
```json
{
  "status": "ok",
  "model": "llama3-8b-8192"
}
```

## Error Handling
If the LLM call fails, the API returns a clean error response with status code 500 and an error message. The server does not crash.