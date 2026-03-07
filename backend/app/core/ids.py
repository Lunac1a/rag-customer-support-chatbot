import uuid

def make_chunk_id(filename: str, chunk_index: int) -> str:
    safe_name = filename.replace(" ", "_")
    return f"{safe_name}_chunk_{chunk_index}_{uuid.uuid4().hex[:8]}"
