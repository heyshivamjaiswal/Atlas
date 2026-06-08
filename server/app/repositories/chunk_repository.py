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