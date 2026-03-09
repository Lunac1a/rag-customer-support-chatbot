from app.core.config import settings
from app.core.embeddings import embed_text
from app.core.logger import get_logger
from app.core.reranker import rerank
from app.core.vectorstore import query_documents
from app.services.llm_service import generate_answer

logger = get_logger(__name__)


def answer_question(question: str) -> dict:
    try:
        logger.info("Received question: %s", question)
        query_embedding = embed_text(question)
        results = query_documents(query_embedding, n_results=settings.RETRIEVAL_TOP_K)

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        if len(metadatas) < len(documents):
            metadatas = metadatas + [{} for _ in range(len(documents) - len(metadatas))]

        structured_documents = []
        for doc, meta in zip(documents, metadatas):
            metadata = meta or {}
            structured_documents.append(
                {
                    "content": doc,
                    "source": metadata.get("source"),
                    "chunk_index": metadata.get("chunk_index"),
                }
            )

        logger.info("Retrieved %d documents", len(structured_documents))

        if not structured_documents:
            return {
                "question": question,
                "answer": "I can not find the answer in the knowledge base.",
                "sources": [],
            }

        final_docs = rerank(question, structured_documents, top_k=settings.FINAL_TOP_K)
        logger.info("Reranked to %d documents", len(final_docs))

        context = "\n\n".join(item["content"] for item in final_docs)

        prompt = f"""
    You are a helpful customer support assistant.

    Answer the user's question ONLY using the context below.
    If the answer is not in the context, say:
    "I can not find the answer in the knowledge base."

    Context:
    {context}

    Question:
    {question}
    """

        logger.info("Sending prompt to LLM")
        answer = generate_answer(prompt)
        logger.info("LLM response generated")

        return {
            "question": question,
            "answer": answer.strip(),
            "sources": [
                {
                    "source": item.get("source"),
                    "chunk_index": item.get("chunk_index"),
                    "text": item.get("content"),
                    "content": item.get("content"),
                    "score": item.get("score"),
                }
                for item in final_docs
            ],
        }
    except Exception:
        logger.exception("Error while answering question")
        raise
