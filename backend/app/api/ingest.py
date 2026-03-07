from fastapi import APIRouter, HTTPException, File, UploadFile
from pydantic import BaseModel

from app.core.embeddings import embed_texts
from app.core.ids import make_chunk_id
from app.core.vectorstore import add_documents
from app.rag.chunker import chunk_text

router = APIRouter(prefix="/api")

class IngestRequest(BaseModel):
    file_path: str

@router.post("/ingest")
async def ingest_file(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Filename is missing.")

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

    chunks = chunk_text(text)

    if not chunks:
        raise HTTPException(status_code=400, detail="No chunks were created from the document.")

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

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to ingest document: {str(e)}")

    return {
        "message": "File ingested successfully.",
        "filename": file.filename,
        "num_chunks": len(chunks),
        "chunk_preview": chunks[:2],
    }
