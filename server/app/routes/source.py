from fastapi import APIRouter, UploadFile, File
from typing import Optional

from app.schemas.source import (
    WebsiteSource,
    SourceResponse
)

from app.services.source.source_service import (
    process_website,
    fetch_source,
    fetch_sources,
    process_pdf_source,
)

router = APIRouter(
    prefix="/source",
    tags=["source"]
)


@router.get("/")
def get_source(
    type: Optional[str] = None
):

    sources = fetch_sources()

    if type:

        return [
            source
            for source in sources
            if source["type"] == type
        ]

    return sources


@router.get("/{source_id}")
def get_single_source(
    source_id: int
):

    return fetch_source(
        source_id
    )


@router.post("/pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    return await process_pdf_source(
        file
    )


@router.post(
    "/web",
    response_model=SourceResponse
)
def add_website(
    data: WebsiteSource
):

    return process_website(
        data.url
    )


@router.post("/youtube")
def add_youtube():

    return {
        "message": "youtube endpoint"
    }