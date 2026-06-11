from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import (
    get_db
)

from app.schemas.query import (
    QueryRequest,
    QueryResponse
)

from app.services.llm.rag_service import (
    answer_query
)

router = APIRouter(
    prefix="/query",
    tags=["query"]
)


@router.post(
    "/",
    response_model=QueryResponse
)
def ask_query(
    data: QueryRequest,
    db: Session = Depends(get_db)
):

    return answer_query(
        query=data.query,
        source_type=data.source_type,
        source_id=data.source_id,
        db=db
    )
