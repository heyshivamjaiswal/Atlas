from qdrant_client.models import (
    PointStruct,
    Filter,
    FieldCondition,
    MatchValue,
    MatchAny
)

import uuid

from app.services.vector.qdrant_connection import client

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
                    "source_type": chunk["source_type"],
                    "user_id": chunk["user_id"]
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
    user_id: int | None = None,
    source_ids: list[int] | None = None
):

    conditions = []

    if user_id:

        conditions.append(
            FieldCondition(
                key="user_id",
                match=MatchValue(
                    value=user_id
                )
            )
        )

    if source_ids:

        conditions.append(
            FieldCondition(
                key="source_id",
                match=MatchAny(
                    any=source_ids
                )
            )
        )

    query_filter = None

    if conditions:

        query_filter = Filter(
            must=conditions
        )
        print("\n===== QDRANT FILTER =====")
        print(query_filter)

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=limit,
        query_filter=query_filter
    )
    print("\n===== QDRANT RESULTS =====")
    print(len(response.points))

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
