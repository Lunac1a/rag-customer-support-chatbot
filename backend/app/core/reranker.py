from sentence_transformers import CrossEncoder

MODEL_NAME = "BAAI/bge-reranker-base"

_model = CrossEncoder(MODEL_NAME)

def rerank(query: str, documents: list[str], top_k: int = 3):
    pairs = [[query, doc] for doc in documents]

    scores = _model.predict(pairs)

    ranked = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [doc for doc, _ in ranked[:top_k]]
