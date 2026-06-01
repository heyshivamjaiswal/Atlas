from fastapi import HTTPException

from app.repositories.source_repository import (
    add_source,
    get_source,
    get_source_by_id,
)

def process_website(url: str):

    source = {
        "id": len(get_source()) + 1,
        "type": "website",
        "url": str(url)
    }
 
    return add_source(source)


def fetch_sources():

    return get_source()


def fetch_source(source_id: int):

    source = get_source_by_id(source_id)

    if source is None:

        raise HTTPException(
            status_code=404,
            detail="Source not found"
        )

    return source