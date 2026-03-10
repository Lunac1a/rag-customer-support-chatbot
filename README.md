# RAG Customer Support Chatbot

A **local Retrieval-Augmented Generation (RAG) chatbot** built with
**FastAPI, React, Chroma, BGE embeddings/reranker, and Ollama**.

The system allows users to upload knowledge-base documents, retrieve
relevant chunks with semantic search, rerank them, and generate grounded
answers with source references.

------------------------------------------------------------------------

## Features

-   Upload `.txt` knowledge-base documents
-   Automatic chunking, embedding, and storage in **Chroma**
-   Semantic retrieval using vector search
-   Reranking of retrieved chunks before generation
-   Local LLM answer generation using **Ollama**
-   Answers include supporting **source chunks**
-   Configurable backend settings via `.env`
-   Configurable frontend API host/port via `.env`
-   Centralized logging to console and `logs/app.log`

------------------------------------------------------------------------

## Tech Stack

**Backend** - FastAPI - ChromaDB - Sentence Transformers (BGE) - BGE
Reranker - Ollama - Python / dotenv

**Frontend** - React - Vite

------------------------------------------------------------------------

## Project Structure

    rag-customer-support-chatbot
    ├── backend
    │   ├── app
    │   │   ├── api
    │   │   ├── core
    │   │   ├── services
    │   │   └── rag
    │   ├── .env.example
    │   └── requirements.txt
    ├── frontend
    │   ├── src
    │   ├── .env.example
    │   └── package.json
    └── README.md

------------------------------------------------------------------------

## RAG Pipeline

    Upload document
        ↓
    Chunk text
        ↓
    Generate embeddings
        ↓
    Store in Chroma
        ↓
    User asks question
        ↓
    Embed question
        ↓
    Retrieve top-k chunks
        ↓
    Rerank retrieved chunks
        ↓
    Build prompt
        ↓
    Generate answer with Ollama
        ↓
    Return answer + sources

------------------------------------------------------------------------

## API Endpoints

`GET /` -- backend root check\
`POST /api/health` -- health check\
`POST /api/ingest` -- upload `.txt` → chunk → embed → store\
`POST /api/query` -- vector retrieval only\
`POST /api/chat` -- full RAG pipeline

------------------------------------------------------------------------

## Configuration

### Backend

    cd backend
    cp .env.example .env

Example:

    OLLAMA_BASE_URL=http://localhost:11434
    OLLAMA_MODEL=qwen2.5:7b

    EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
    RERANK_MODEL=BAAI/bge-reranker-base

    CHROMA_DIR=./chroma_db

    CHUNK_SIZE=500
    CHUNK_OVERLAP=50

    RETRIEVAL_TOP_K=10
    FINAL_TOP_K=3

### Frontend

    cd frontend
    cp .env.example .env

Example:

    VITE_API_HOST=127.0.0.1
    VITE_API_PORT=8000

------------------------------------------------------------------------

## Local Setup

### Clone repository

    git clone <repo-url>
    cd rag-customer-support-chatbot

### Backend

    cd backend
    python -m venv .venv
    source .venv/bin/activate     # macOS / Linux
    .venv\Scripts\activate      # Windows
    pip install -r requirements.txt
    uvicorn app.main:app --reload

### Ollama

    ollama pull qwen2.5:7b
    ollama serve

### Frontend

    cd frontend
    npm install
    npm run dev

------------------------------------------------------------------------

## Usage

1.  Open the frontend in your browser\
2.  Upload a `.txt` knowledge-base file\
3.  Ask questions in the chat UI\
4.  The system retrieves, reranks, generates an answer, and returns
    sources

------------------------------------------------------------------------

## Logging

Logs are written to:

    logs/app.log

and printed to the console.

------------------------------------------------------------------------

## Limitations

-   Only `.txt` ingestion
-   Single-user local setup
-   No authentication
-   No streaming responses

------------------------------------------------------------------------

## Possible Improvements

-   PDF / Markdown ingestion
-   Streaming responses
-   Better UI polish
-   Automated tests
-   Docker deployment

------------------------------------------------------------------------

## Purpose

Demonstrates:

-   end-to-end RAG pipeline
-   local LLM integration
-   semantic retrieval + reranking
-   frontend/backend integration
-   engineering improvements beyond a simple demo
