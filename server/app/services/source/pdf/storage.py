from pathlib import Path

UPLOAD_DIR = Path("storage/uploads/pdfs")

UPLOAD_DIR.mkdir(
    parents=True,

    exist_ok=True
)


def save_pdf_file(
        file_name : str,
        content: bytes
):
    
    file_path = (
        UPLOAD_DIR / file_name
    )

    with open(
        file_path,
        "wb"
    ) as file:

        file.write(
            content
        )

    return str(
        file_path
    )