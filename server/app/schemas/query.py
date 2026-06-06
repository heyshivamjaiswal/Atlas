from pydantic import BaseModel, Field
from typing import List, Optional


class SourceMetadata(
    BaseModel
):
    source: str
    page: int | None = None
    score: float | None = None


class QueryRequest(
    BaseModel
):
    query: str
    source_type: Optional[str] = None


class QueryResponse(
    BaseModel
):
    answer: str

    sources: List[SourceMetadata] = Field(
        default_factory=list
    )