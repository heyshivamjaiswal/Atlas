from app.services.storage.supabase_storage import (
    supabase
)

print(
    supabase.storage.list_buckets()
)
