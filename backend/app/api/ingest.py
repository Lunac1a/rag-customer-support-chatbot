from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.rag.loader import load_txt_file
from app.rag.chunker import split_text

router = APIRouter(prefix="/api")

class IngestRequest(BaseModel):
    file_path: str

@router.post("/ingest")
def ingest_document(request: IngestRequest):
    try:
        path = Path(request.file_path)

        if not path.exists():
            raise HTTPException(status_code=404, detail="File not found")

        text = load_txt_file(request.file_path)
        chunks = split_text(text)

        return {
            "message": "Document loaded and chunked successfully",
            "file_name": path.name,
            "num_chunks": len(chunks),
            "preview": chunks[:2]
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
