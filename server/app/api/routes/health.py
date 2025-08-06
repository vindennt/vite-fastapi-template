from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health check"])

# Simple health check endpoint
@router.get("/ping")
async def ping():
    return {"message": "pong"}