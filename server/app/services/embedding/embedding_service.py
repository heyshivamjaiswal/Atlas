from langchain_ollama import OllamaEmbeddings

from app.core.settings import (
    OLLAMA_EMBEDDING_MODEL
)

embedding_model = OllamaEmbeddings(
    model=OLLAMA_EMBEDDING_MODEL
)


def embed_chunks(chunks):

    text = [
        chunk["content"]
        for chunk in chunks
    ]

    vectors = embedding_model.embed_documents(text)

    return vectors
