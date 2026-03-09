from sentence_transformers import SentenceTransformer
from app.core.config import settings

_model = SentenceTransformer(settings.EMBEDDING_MODEL)

def get_embedding_model() -> SentenceTransformer:
    return _model

def embed_text(text: str) -> list[float]:
    embedding = _model.encode(text, normalize_embeddings=True)
    return embedding.tolist()

def embed_texts(texts: list[str]) -> list[list[float]]:
    embedding = _model.encode(texts, normalize_embeddings=True)
    return embedding.tolist()
