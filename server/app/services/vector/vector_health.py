from app.services.vector.qdrant_connection import client

from app.services.vector.init_qdrant import (
    create_collection
)

from app.core.logger import (
    logger
)

COLLECTION_NAME = "atlas_chunks"


def ensure_collection_exists():

    if not client.collection_exists(
        collection_name=COLLECTION_NAME
    ):

        logger.warning(
            "Qdrant collection missing. Creating collection."
        )

        create_collection()

    try:

        count = client.count(
            collection_name=COLLECTION_NAME,
            exact=True
        )

        logger.info(
            f"Qdrant collection={COLLECTION_NAME}"
        )

        logger.info(
            f"Vector count={count.count}"
        )

    except Exception as e:

        logger.error(
            f"Qdrant health check failed: {e}"
        )
