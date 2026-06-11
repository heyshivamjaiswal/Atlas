from qdrant_client.models import (
    PointStruct,
    Filter,
    FieldCondition,
    MatchValue
)

import uuid

from app.services.vector.qdrant_client import client

COLLECTION_NAME = "atlas_chunks"


def add_vectors(
    chunks
):

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
                    "source_id": chunk["source_id"],
                    "source_type": chunk["source_type"]
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )


def search_vectors(
    query_vector,
    limit=5,
    source_type: str | None = None,
    source_id: int | None = None
):

    conditions = []

    if source_type:

        conditions.append(
            FieldCondition(
                key="source_type",
                match=MatchValue(
                    value=source_type
                )
            )
        )

    if source_id:

        conditions.append(
            FieldCondition(
                key="source_id",
                match=MatchValue(
                    value=source_id
                )
            )
        )

    query_filter = None

    if conditions:

        query_filter = Filter(
            must=conditions
        )

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=limit,
        query_filter=query_filter
    )

    return response.points


def delete_vectors_by_source_id(
    source_id: int
):

    client.delete(
        collection_name=COLLECTION_NAME,

        points_selector=Filter(
            must=[
                FieldCondition(
                    key="source_id",
                    match=MatchValue(
                        value=source_id
                    )
                )
            ]
        )
    )
