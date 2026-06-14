from app.services.storage.supabase_storage import (
    upload_pdf
)

with open(
    "storage/uploads/pdfs/Introduction to Docker.pdf",
    "rb"
) as file:

    result = upload_pdf(
        "Introduction to Docker.pdf",
        file.read()
    )

print(result)
