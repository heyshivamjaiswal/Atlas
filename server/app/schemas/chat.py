from pydantic import BaseModel


class CreateChatRequest(BaseModel):
    title: str


class ChatResponse(BaseModel):
    id: int
    title: str


class MessageResponse(BaseModel):
    role: str
    content: str
