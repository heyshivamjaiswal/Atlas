from app.database.connection import SessionLocal

from app.repositories.chunk_repository import (
    get_all_chunks
)

from app.repositories.vector_repository import (
    add_vectors
)

from app.services.embedding.embedding_service import (
    embedding_model
)

from app.services.vector.qdrant_connection import (
    client
)

from app.services.vector.init_qdrant import (
    create_collection
)


COLLECTION_NAME = "atlas_chunks"


def main():

    db = SessionLocal()

    chunks = get_all_chunks(db)

    print(
        f"Found {len(chunks)} chunks"
    )

    mapped_chunks = []

    for chunk in chunks:

        mapped_chunks.append({

            "content": chunk.content,

            "page": chunk.page,

            "source_id": chunk.source_id,

            "source": "reindexed",

            "source_type": "pdf",

            "user_id": 1
        })

    print(
        "Generating embeddings..."
    )

    vectors = embedding_model.embed_documents(
        [
            chunk["content"]
            for chunk in mapped_chunks
        ]
    )

    embedded_chunks = []

    for chunk, vector in zip(
        mapped_chunks,
        vectors
    ):

        embedded_chunks.append({
            **chunk,
            "embedding": vector
        })

    print(
        "Recreating collection..."
    )

    if client.collection_exists(
        COLLECTION_NAME
    ):

        client.delete_collection(
            COLLECTION_NAME
        )

    create_collection()

    print(
        "Uploading vectors..."
    )

    add_vectors(
        embedded_chunks
    )

    count = client.count(
        collection_name=COLLECTION_NAME,
        exact=True
    )

    print(
        f"Vector count = {count.count}"
    )


if __name__ == "__main__":

    main()
