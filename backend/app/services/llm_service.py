import requests
from app.core.config import settings

def generate_answer(prompt: str) -> str:
    response = requests.post(
        settings.OLLAMA_BASE_URL,
        json={
            "model": settings.OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=120,
    )

    response.raise_for_status()
    data = response.json()
    return data["response"]
