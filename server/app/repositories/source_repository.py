from pathlib import Path

UPLOAD_DIR = Path("storage/uploads/pdfs")

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)

def save_pdf_file(file_name: str, content: bytes):
    file_path = UPLOAD_DIR / file_name
    
    with open(file_path , "wb") as file:
        file.write(content)

    return str(file_path)

    
source_db : list = []

def add_source(source: dict):
    source_db.append(source)

    return source

def get_source():
    return source_db

def get_source_by_id(source_id: int):
    for source in source_db:
        if source["id"] == source_id:
            return source

    return None    



chunk_db : list = []

def add_chunk(
        chunk: list
):
    chunk_db.extend(chunk)
    return chunk

def get_chunk():
    return chunk_db

def get_chunk_count():

    return len(chunk_db)




vector_db : list = []

def add_vectors(vectors):
    
    vector_db.extend(vectors)

    return vectors


def get_vectors():
    return vector_db

def get_vector_count():

    return len(vector_db)