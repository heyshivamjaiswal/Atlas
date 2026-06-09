from langchain_ollama import (
    ChatOllama
)

llm = ChatOllama(
    model="qwen:7b"
)


def ask_llm(
    prompt: str
):

    response = llm.invoke(
        prompt
    )

    return response.content