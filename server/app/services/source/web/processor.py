from sqlalchemy.orm import Session

from app.services.source.web.validator import (
    validate_url
)

from app.services.source.web.loader import (
    load_web_document
)

from app.services.source.pdf.splitter import (
    create_chunks as split_chunks
)

from app.services.source.pdf.chunk_mapper import (
    map_chunks
)

from app.repositories.source_repository import (
    create_source
)

from app.repositories.chunk_repository import (
    create_chunks as create_chunk_records
)

from app.services.embedding.embedding_service import (
    embed_chunks
)

from app.repositories.vector_repository import (
    add_vectors
)


def process_website(
    url: str,
    db: Session
):

    # validate
    validate_url(url)

    # load website
    docs = load_web_document(url)

    # split
    chunks = split_chunks(docs)

    # create source
    source = create_source(
        db=db,
        user_id=1,  # temporary
        source_type="website",
        title=url,
        file_name=None
    )

    # map chunks
    mapped_chunks = map_chunks(
        chunks,
        url,
        source.id
    )

    # store chunks
    create_chunk_records(
        db=db,
        chunks=mapped_chunks
    )

    # embeddings
    vectors = embed_chunks(
        mapped_chunks
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

    # qdrant
    add_vectors(
        embedded_chunks
    )

    return {
        "source_id": source.id,
        "url": url,
        "chunks": len(mapped_chunks),
        "embeddings": len(vectors)
    }