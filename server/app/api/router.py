from fastapi import APIRouter
from app.api.routes import health, auth, item

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(item.router)