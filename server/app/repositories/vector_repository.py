from qdrant_client.models import PointStruct
import uuid

from app.services.vector.qdrant_client import client

COLLECTION_NAME = "atlas_chunks"


def add_vectors(chunks):

    points = []

    for chunk in chunks:

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=chunk["embedding"],
                payload={
                    "content": chunk["content"],
                    "source": chunk["source"],
                    "page": chunk["page"],
                    "source_id": chunk["source_id"]
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )


def search_vectors(
    query_vector,
    limit=5
):

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=limit
    )

    return response.points