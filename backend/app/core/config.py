import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # LLM
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

    # Embedding
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

    # Reranker
    RERANK_MODEL = os.getenv("RERANK_MODEL")

    # Vector DB
    CHROMA_DIR = os.getenv("CHROMA_DIR")

    # Chunking
    CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))
    CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP"))

    # Retrieval
    RETRIEVAL_TOP_K = int(os.getenv("RETRIEVAL_TOP_K"))
    FINAL_TOP_K = int(os.getenv("FINAL_TOP_K"))

    # React
    ORIGINS_PORT = int(os.getenv("ORIGINS_PORT"))


settings = Settings()
