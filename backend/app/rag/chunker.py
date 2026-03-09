from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.core.config import settings

def chunk_text(
        text: str,
        chunk_size: int,
        chunk_overlap: int
) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    return splitter.split_text(text)
