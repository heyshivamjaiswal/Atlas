from app.services.llm.gemini_service import (
    ask_gemini
)


def ask_llm(
    prompt: str
):

    return ask_gemini(
        prompt
    )
