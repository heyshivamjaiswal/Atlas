from fastapi import (
    APIRouter,
    Depends
)

from app.schemas.debug import (
    RetrievalRequest
)

from app.services.auth.current_user import (
    get_current_user
)

from app.services.retrieval.debug_service import (
    debug_retrieval
)

router = APIRouter(
    prefix="/debug",
    tags=["debug"]
)


@router.post("/retrieve")
def retrieve_debug(
    data: RetrievalRequest,
    current_user=Depends(
        get_current_user
    )
):

    return debug_retrieval(
        data.query,
        current_user.id
    )
