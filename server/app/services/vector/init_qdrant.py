from qdrant_client.models import (
    VectorParams,
    Distance
)

from app.services.vector.qdrant_client import (
    client
)


def create_collection():

    collections = client.get_collections()

    existing = [

        c.name

        for c in collections.collections
    ]

    if "atlas_chunks" in existing:

        print(
            "Collection already exists"
        )

        return

    client.create_collection(

        collection_name="atlas_chunks",

        vectors_config=VectorParams(

            size=768,

            distance=Distance.COSINE
        )
    )

    print(
        "Collection created"
    )


if __name__ == "__main__":

    create_collection()