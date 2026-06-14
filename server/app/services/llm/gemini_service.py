from google import genai

from app.core.settings import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)

client = genai.Client(
    api_key=GEMINI_API_KEY
)


def ask_gemini(
    prompt: str
) -> str:

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text
