from app.core.embeddings import embed_text
from app.core.vectorstore import query_documents
from app.services.llm import generate_answer

def answer_question(question: str) -> dict:
    query_embedding = embed_text(question)
    results = query_documents(query_embedding, n_results=3)

    documents = results["documents"][0]
    context = "\n\n".join(documents)

    prompt = f"""
    You are a customer support assistant.
    Answer the user's question only based on the context below.
    If the answer is not in the context, say you don't know.
    
    Context:
    {context}
    
    Question:
    {question}
    """

    answer = generate_answer(prompt)

    return {
        "question": question,
        "answer": answer,
        "sources": documents
    }
