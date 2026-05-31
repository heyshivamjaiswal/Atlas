from pydantic import BaseModel , HttpUrl

class WebsiteSource(BaseModel):
    url: HttpUrl


class SourceResponse(BaseModel):
    id: int 
    type: str
    url: str