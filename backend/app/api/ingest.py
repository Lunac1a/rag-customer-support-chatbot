from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel

from app.core.config import settings
from app.core.embeddings import embed_texts
from app.core.ids import make_chunk_id
from app.core.logger import get_logger
from app.core.vectorstore import add_documents
from app.rag.chunker import chunk_text

router = APIRouter(prefix="/api")
logger = get_logger(__name__)


class IngestRequest(BaseModel):
    file_path: str


@router.post("/ingest")
async def ingest_file(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is missing.")

    logger.info("Received file upload: %s", file.filename)

    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files are supported for now.")

    try:
        raw_bytes = await file.read()
        text = raw_bytes.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File must be UTF-8 encoded text.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read file: {str(e)}")

    if not text.strip():
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    chunks = chunk_text(text, settings.CHUNK_SIZE, settings.CHUNK_OVERLAP)

    if not chunks:
        raise HTTPException(status_code=400, detail="No chunks were created from the document.")

    chunk_count = len(chunks)
    logger.info("Split document into %d chunks", chunk_count)

    ids = []
    metadatas = []

    for i, chunk in enumerate(chunks):
        ids.append(make_chunk_id(file.filename, i))
        metadatas.append(
            {
                "source": file.filename,
                "chunk_index": i,
            }
        )

    try:
        embeddings = embed_texts(chunks)

        add_documents(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
        )
        logger.info("Stored %d chunks in vector database", chunk_count)

    except Exception as e:
        logger.exception("Failed to ingest document")
        raise HTTPException(status_code=500, detail=f"Failed to ingest document: {str(e)}")

    return {
        "message": "File ingested successfully.",
        "filename": file.filename,
        "num_chunks": chunk_count,
        "chunk_preview": chunks[:2],
    }
