from fastapi import APIRouter
from pydantic import BaseModel

from app.core.vectorstore import query_documents
from app.core.embeddings import embed_text

router = APIRouter(prefix="/api")

class QueryRequest(BaseModel):
    question: str

@router.post("/query")
def query_docs(request: QueryRequest):

    # generate query embedding
    query_embedding = embed_text(request.question)

    # vector search
    results = query_documents(query_embedding)

    # return documents
    documents = results["documents"][0]

    return {
        "question": request.question,
        "top_chunks": documents
    }
