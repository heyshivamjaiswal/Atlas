from fastapi import HTTPException , UploadFile

MAX_FILE_SIZE =  5 * 1024 * 1024

async def validator_pdf(file: UploadFile):
    


    if file.content_type != "application/pdf":

        raise HTTPException(
            status_code=400,
            detail="Only PDF file allowed"
        )
    
    content = await file.read()

    if len(content) > MAX_FILE_SIZE:

        raise HTTPException(
            status_code=400,
            detail="File exceeds 5MB limit"
        )
    
    return content