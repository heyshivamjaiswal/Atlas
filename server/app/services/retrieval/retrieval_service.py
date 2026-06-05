from app.services.embedding.embedding_service import embedding_model
from app.repositories.source_repository import get_vectors

import numpy as np


def embed_query(
    query: str
):

    return embedding_model.embed_query(
        query
    )


def cosine_similarity(
    a,
    b
):

    a = np.array(a)

    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a)
        * np.linalg.norm(b)
    )


def retrieve_chunks(
    query: str,
    top_k: int = 3
):

    query_vector = embed_query(
        query
    )

    stored_vectors = get_vectors()

    scored = []

    for item in stored_vectors:

        similarity = cosine_similarity(
            query_vector,
            item["embedding"]
        )

        scored.append({
            "score": similarity,
            "chunk": item
        })

    scored.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scored[:top_k]