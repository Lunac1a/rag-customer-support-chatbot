from pathlib import Path
from typing import Any

import chromadb

CHROMA_PATH = Path("./chroma_db")
COLLECTION_NAME = "support_docs"

_client = chromadb.PersistentClient(path=str(CHROMA_PATH))
_collection = _client.get_or_create_collection(name=COLLECTION_NAME)

def get_chroma_client():
    return _client

def get_collection():
    return _collection

def add_documents(
        ids: list[str],
        documents: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict[str, Any]] | None = None,
) -> None:
    _collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
    )

def query_documents(
        query_embedding: list[float],
        n_results: int = 3,
):
    results = _collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
    )
    return results
