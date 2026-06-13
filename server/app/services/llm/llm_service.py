from langchain_ollama import (
    ChatOllama
)

from app.core.settings import (
    OLLAMA_CHAT_MODEL
)

llm = ChatOllama(
    model=OLLAMA_CHAT_MODEL
)


def ask_llm(
    prompt: str
):

    response = llm.invoke(
        prompt
    )

    return response.content
