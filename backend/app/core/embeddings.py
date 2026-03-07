from sentence_transformers import SentenceTransformer

MODEL_NAME = "BAAI/bge-small-en-v1.5"

_model = SentenceTransformer(MODEL_NAME)

def get_embedding_model() -> SentenceTransformer:
    return _model

def embed_text(text: str) -> list[float]:
    embedding = _model.encode(text, normalize_embeddings=True)
    return embedding.tolist()

def embed_texts(texts: list[str]) -> list[list[float]]:
    embedding = _model.encode(texts, normalize_embeddings=True)
    return embedding.tolist()
