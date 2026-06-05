from fastapi import HTTPException ,UploadFile
from pypdf import PdfReader 


from app.repositories.source_repository import (
    save_pdf_file,
)

from app.repositories.source_repository import (
    add_source,
    get_source,
    get_source_by_id,
)

MAX_FILE_SIZE = 5 * 1024 * 1024

def extract_pdf_text(file_path: str):
    reader = PdfReader(file_path)

    extract_text = ""

    for page in reader.pages:
        page_text =  page.extract_text()

        if page_text:

            extract_text += page_text + "\n"

        return extract_text    

async def process_pdf(file: UploadFile):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files allowed"
        )
    
    content = await file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File exceed 5MB limit"
        )

    file_path = save_pdf_file(
        file.filename,
        content
    )

    text = extract_pdf_text(
        file_path
    )

    return{
        "file_name" : file.filename,
        "path": file_path,
        "characters": len(text),
        "preview": text[:500]
    }

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

