from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.models.schemas import QueryRequest, QueryResponse
from api.services.llm_service import call_llm, MODEL_NAME

router = APIRouter()


@router.post("/ask", response_model=QueryResponse)
async def ask(request: QueryRequest):
    try:
        response_text, latency_ms = await call_llm(request.query)
        return QueryResponse(
            response=response_text,
            model=MODEL_NAME,
            latency_ms=round(latency_ms, 2),
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"LLM call failed: {str(e)}"},
        )


@router.get("/health")
async def health():
    return {"status": "ok", "model": MODEL_NAME}