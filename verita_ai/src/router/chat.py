from fastapi import APIRouter
from pydantic import BaseModel
from src.model.llm import generate_answer

router = APIRouter()

class ChatInput(BaseModel):
    message: str

@router.post("/")
def chat(chat_input: ChatInput):
    answer = generate_answer(chat_input.message)

    return {
        "response": answer
    }