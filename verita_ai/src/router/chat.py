from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ChatInput(BaseModel):
    message: str


@router.post("/")
def chat(chat_input: ChatInput):
    return {"response": "Hi, welcome to Verita"}