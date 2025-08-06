from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.router import api_router
from app.core.db import engine, init_db
from sqlmodel import Session

app = FastAPI()

if settings.all_cors_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)

@app.get("/", tags=["root"])
async def root():
    return {"message": "\/   /\     /   O   \      /O\  "}

@app.on_event("startup")
def on_startup():
    with Session(engine) as session:
        init_db(session)