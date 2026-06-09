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
    process_website
)

from app.schemas.source import (
    WebsiteSource,
    SourceResponse
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
    "/web",

    response_model=SourceResponse
)
def add_website(

    data: WebsiteSource
):

    return process_website(
        data.url
    )


@router.post(
    "/youtube"
)
def add_youtube():

    return {

        "message": "youtube endpoint"
    }