import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # LLM
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")

    # Embedding
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "BAAI/bge-small-en-v1.5")

    # Reranker
    RERANK_MODEL = os.getenv("RERANK_MODEL", "BAAI/bge-reranker-base")

    # Vector DB
    CHROMA_DIR = os.getenv("CHROMA_DIR", "./chroma_db")

    # Chunking
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))

    # Retrieval
    RETRIEVAL_TOP_K = int(os.getenv("RETRIEVAL_TOP_K", 10))
    FINAL_TOP_K = int(os.getenv("FINAL_TOP_K", 3))


settings = Settings()
