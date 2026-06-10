from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.services.source.pdf.processor import (
    process_pdf
)

from app.services.source.web.processor import (
    process_website as process_website_source
)

from app.services.source.youtube.processor import (
    process_youtube as youtube_processor
)

async def process_pdf_source(
    file: UploadFile,
    db: Session
):

    return await process_pdf(
        file,
        db
    )


def process_website(
    url: str,
    db: Session
):

    return process_website_source(
        url,
        db
    )


def  process_youtube_source(
        url:str,
        db:Session
):
    return youtube_processor(
        url,
        db
    )