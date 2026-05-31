from fastapi import APIRouter

from app.schemas.source import WebsiteSource
from app.services.source_service import (
    process_website, 
    get_all_sources
    )


router = APIRouter(
    prefix="/source",
    tags=["source"]
)

@router.get("/")
def get_source():
    return get_all_sources()

@router.post("/pdf")
def upload_pdf():
    return{
        "message": "pdf endpoint"
    }

@router.post("/web")
def add_website(data: WebsiteSource):
    return process_website(data.url)

@router.post("/youtube")
def add_youtube():
    return{
        "message": "youtube endpoint"
    
}