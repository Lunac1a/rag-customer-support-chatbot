from app.core.embeddings import embed_text
from app.core.vectorstore import query_documents
from app.services.llm import generate_answer
from app.core.reranker import rerank

def answer_question(question: str) -> dict:
    query_embedding = embed_text(question)
    results = query_documents(query_embedding, n_results=10)

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        return {
            "question": question,
            "answer": "I can not find the answer in the knowledge base.",
            "sources": []
        }

    # rerank
    top_docs = rerank(question, documents, top_k=3)

    context = "\n\n".join(top_docs)

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

    answer = generate_answer(prompt)

    return {
        "question": question,
        "answer": answer.strip(),
        "sources": [
            {
                "source": meta.get("source"),
                "chunk_index": meta.get("chunk_index"),
                "text": doc
            }
            for doc, meta in zip(documents, metadatas)
        ]
    }
