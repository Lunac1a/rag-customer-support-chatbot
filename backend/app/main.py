from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.ingest import router as ingest_router

app = FastAPI()
app.include_router(health_router)
app.include_router(ingest_router)

@app.get("/")
def root():
    return {"message": "backend running"}