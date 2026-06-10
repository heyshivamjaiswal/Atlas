from langchain_ollama import (
    ChatOllama
)

llm = ChatOllama(
    model="llama3.2:3b"
)


def ask_llm(
    prompt: str
):

    response = llm.invoke(
        prompt
    )

    return response.content