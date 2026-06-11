from sqlalchemy.orm import Session

from app.models.chunk import Chunk


def create_chunks(
    db: Session,
    chunks: list
):

    db_chunks = [

        Chunk(
            source_id=item["source_id"],
            chunk_index=item["chunk_index"],
            content=item["content"],
            page=item["page"]
        )

        for item in chunks
    ]

    db.add_all(db_chunks)

    db.commit()

    return db_chunks


def count_chunks_by_source_id(
    db: Session,
    source_id: int
):

    return (
        db.query(Chunk)
        .filter(
            Chunk.source_id == source_id
        )
        .count()
    )


def delete_chunks_by_source_id(
    db: Session,
    source_id: int
):

    (
        db.query(Chunk)
        .filter(
            Chunk.source_id == source_id
        )
        .delete()
    )

    db.commit()


def get_all_chunks(
    db: Session
):

    return (
        db.query(Chunk)
        .all()
    )
