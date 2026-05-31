from fastapi import APIRouter

router = APIRouter(
    prefix="/source",
    tags=["source"]
)

@router.get("/")
def get_source():
    return{
        "message": []
    }

@router.post("/pdf")
def upload_pdf():
    return{
        "message": "pdf endpoint"
    }

@router.post("/web")
def add_website():
    return{
        "message": "website endpoint"
    }

@router.post("/youtube")
def add_youtube():
    return{
        "message": "youtube endpoint"
    
}