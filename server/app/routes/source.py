from fastapi import APIRouter

from app.schemas.source import(
     WebsiteSource, 
     SourceResponse 
)
from app.services.source_service import (
    process_website, 
    fetch_source,
    )


router = APIRouter(
    prefix="/source",
    tags=["source"]
)

@router.get("/")
def get_source():
    return fetch_source()

@router.get("/{source_id}")
def get_single_source(source_id: int):

    return fetch_source(source_id)

@router.post("/pdf")
def upload_pdf():
    return{
        "message": "pdf endpoint"
    }

@router.post("/web" , response_model=SourceResponse)

def add_website(data: WebsiteSource):
    return process_website(data.url)

@router.post("/youtube")
def add_youtube():
    return{
        "message": "youtube endpoint"
    
}