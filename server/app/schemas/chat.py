from pydantic import BaseModel


class CreateChatRequest(BaseModel):
    title: str
    source_ids: list[int]


class ChatResponse(BaseModel):
    id: int
    title: str


class MessageResponse(BaseModel):
    role: str
    content: str
