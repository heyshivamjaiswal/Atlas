from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.database.dependencies import (
    get_db
)

from app.services.auth.current_user import (
    get_current_user
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
    db: Session = Depends(get_db),

    current_user=Depends(
        get_current_user
    )
):

    return answer_query(
        query=data.query,
        db=db,
        user_id=current_user.id,
        source_type=data.source_type,
        source_id=data.source_id
    )
