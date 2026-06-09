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

        return

    client.create_collection(

        collection_name="atlas_chunks",

        vectors_config=VectorParams(

            size=768,

            distance=Distance.COSINE
        )
    )