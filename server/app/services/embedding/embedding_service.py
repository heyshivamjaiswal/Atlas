from app.services.embedding.hf_embedding_service import (
    embedding_model
)


def embed_chunks(chunks):

    text = [
        chunk["content"]
        for chunk in chunks
    ]

    vectors = embedding_model.embed_documents(
        text
    )

    return vectors
