from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import (
    get_db
)

from app.services.source.source_service import (
    process_pdf_source,
    process_website,
    process_youtube_source
)

from app.schemas.source import (
    WebsiteSource
)

router = APIRouter(

    prefix="/source",

    tags=["source"]
)


@router.post(
    "/pdf"
)
async def upload_pdf(

    file: UploadFile = File(...),

    db: Session = Depends(
        get_db
    )
):

    return await process_pdf_source(

        file,

        db
    )


@router.post(
    "/web"
)
def add_website(

    data: WebsiteSource,

    db: Session = Depends(
        get_db
    )
):

    return process_website(

        str(data.url),

        db
    )


@router.post(
    "/youtube"
)
def add_youtube(

    data: WebsiteSource,

    db: Session = Depends(
        get_db
    )
):

    return process_youtube_source(

        str(data.url),

        db
    ) 