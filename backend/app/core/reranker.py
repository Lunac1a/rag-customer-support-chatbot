from app.core.config import settings
from sentence_transformers import CrossEncoder

_model = CrossEncoder(settings.RERANK_MODEL)


def rerank(query: str, documents: list[dict], top_k: int = 3) -> list[dict]:
    if not documents:
        return []

    pairs = [[query, item["content"]] for item in documents]
    scores = _model.predict(pairs)

    scored_documents = []
    for item, score in zip(documents, scores):
        scored_item = dict(item)
        scored_item["score"] = float(score)
        scored_documents.append(scored_item)

    ranked = sorted(scored_documents, key=lambda item: item["score"], reverse=True)
    return ranked[:top_k]
