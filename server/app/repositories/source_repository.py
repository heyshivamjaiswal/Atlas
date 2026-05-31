source_db = []

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