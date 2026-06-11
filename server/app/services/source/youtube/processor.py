from sqlalchemy.orm import Session

from app.services.source.youtube.validator import (
    validator_youtube
)

from app.services.source.youtube.loader import (
    load_youtube_document
)

from app.services.source.youtube.splitter import (
    create_youtube_chunks
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


def process_youtube(
    url: str,
    db: Session
):

    # validate
    validator_youtube(
        url
    )

    # load transcript
    docs = load_youtube_document(
        url
    )

    # split transcript
    chunks = create_youtube_chunks(
        docs
    )

    # create source
    source = create_source(

        db=db,

        user_id=1,  # temp until auth

        source_type="youtube",

        title=url,

        file_name=None
    )

    # map chunks
    mapped_chunks = map_chunks(

        chunks,

        url,

        source.id,
        "youtube"
    )

    # save chunk records
    create_chunk_records(

        db=db,

        chunks=mapped_chunks
    )

    # embeddings
    embeddings = embed_chunks(
        mapped_chunks
    )

    embedded_chunks = []

    for chunk, embedding in zip(

        mapped_chunks,

        embeddings
    ):

        embedded_chunks.append({

            **chunk,

            "embedding": embedding
        })

    # store vectors
    add_vectors(
        embedded_chunks
    )

    return {

        "source_id": source.id,

        "url": url,

        "chunks": len(
            mapped_chunks
        ),

        "embeddings": len(
            embeddings
        )
    }
