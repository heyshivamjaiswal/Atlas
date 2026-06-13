from app.services.vector.qdrant_connection import client

from app.services.vector.init_qdrant import (
    create_collection
)

COLLECTION_NAME = "atlas_chunks"


def ensure_collection_exists():

    if not client.collection_exists(
        collection_name=COLLECTION_NAME
    ):

        print("\n[QDRANT] Collection missing.")
        print("[QDRANT] Creating collection...")

        create_collection()

    try:

        count = client.count(
            collection_name=COLLECTION_NAME,
            exact=True
        )

        print("\n========== QDRANT ==========")

        print(
            f"Collection: {COLLECTION_NAME}"
        )

        print(
            f"Vector Count: {count.count}"
        )

        print("============================\n")

    except Exception as e:

        print(
            f"[QDRANT] Health check failed: {e}"
        )
