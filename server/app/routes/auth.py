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

from app.services.auth.current_user import (
    get_current_user
)

from app.services.source.source_service import (
    process_pdf_source,
    process_website,
    process_youtube_source
)

from app.services.source.source_management_service import (
    list_sources,
    get_source_details,
    delete_source_service
)

from app.schemas.source import (
    WebsiteSource
)

router = APIRouter(
    prefix="/source",
    tags=["source"]
)


@router.post("/pdf")
async def upload_pdf(

    file: UploadFile = File(...),

    db: Session = Depends(get_db),

    current_user=Depends(
        get_current_user
    )
):

    return await process_pdf_source(

        file=file,

        db=db,

        user_id=current_user.id
    )


@router.post("/web")
def add_website(

    data: WebsiteSource,

    db: Session = Depends(get_db),

    current_user=Depends(
        get_current_user
    )
):

    return process_website(

        str(data.url),

        db,

        current_user.id
    )


@router.post("/youtube")
def add_youtube(

    data: WebsiteSource,

    db: Session = Depends(get_db),

    current_user=Depends(
        get_current_user
    )
):

    return process_youtube_source(

        str(data.url),

        db,

        current_user.id
    )


@router.get("")
def get_sources_endpoint(

    db: Session = Depends(get_db),

    current_user=Depends(
        get_current_user
    )
):

    return list_sources(

        db,

        current_user.id
    )


@router.get("/{source_id}")
def get_source_endpoint(

    source_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(
        get_current_user
    )
):

    return get_source_details(

        db,

        source_id,

        current_user.id
    )


@router.delete("/{source_id}")
def delete_source_endpoint(

    source_id: int,

    db: Session = Depends(get_db),

    current_user=Depends(
        get_current_user
    )
):

    return delete_source_service(

        db,

        source_id,

        current_user.id
    )
