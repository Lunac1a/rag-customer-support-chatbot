from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.ingest import router as ingest_router
from app.api.query import router as query_router
from app.api.chat import router as chat_router

app = FastAPI()
app.include_router(health_router)
app.include_router(ingest_router)
app.include_router(query_router)
app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "backend running"}