from fastapi import APIRouter

from app.schemas.query import QueryRequest, QueryResponse

from app.services.llm.rag_service import answer_query

router = APIRouter(
    prefix="/query",
    tags=["query"]
)


@router.post(
    "/",
    response_model=QueryResponse
)
def ask_query(data: QueryRequest):

     return answer_query(
          query=data.query,
          source_type=data.source_type
   )