import numpy as np

from app.services.embedding.embedding_service import (
    embedding_model
)

from app.repositories.source_repository import (
    get_vectors
)

SIMILARITY_THRESHOLD = 0.45


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
    top_k: int = 5,
    source_type: str | None = None
):

    query_vector = embed_query(
        query
    )

    stored_vectors = get_vectors()

    if source_type:

        stored_vectors = [

            item

            for item in stored_vectors

            if item["type"] == source_type
        ]

    scored = []

    for item in stored_vectors:

        similarity = cosine_similarity(

            query_vector,

            item["embedding"]
        )

        if similarity < SIMILARITY_THRESHOLD:

            continue

        scored.append({

            "score": similarity,

            "chunk": item
        })

    scored.sort(

        key=lambda x: x["score"],

        reverse=True
    )

    retrieved = scored[:top_k]

    print("\n===== RETRIEVED =====")

    for item in retrieved:

        print(
            f"Score: {item['score']}"
        )

        print(
            item["chunk"]["content"][:300]
        )

        print("----------------")

    return retrieved