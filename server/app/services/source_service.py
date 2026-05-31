
source_db = []

def process_website(url: str):

    source = {
        "id": len(source_db) + 1,
        "type": "website",
        "url": str(url)
    }
    source_db.append(source)
    
    return source

def get_all_sources():
    return source_db