from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.core.config import settings

def chunk_text(
        text: str,
        chunk_size: int,
        chunk_overlap: int
) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = settings.CHUNK_SIZE,
        chunk_overlap = settings.CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""]
    )
    return splitter.split_text(text)
