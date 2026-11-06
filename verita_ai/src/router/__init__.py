from fastapi import APIRouter

from .chat import router as chat_router

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)
router.include_router(chat_router)


@router.get("/")
def chat_home():
    return {"message": "Chat API is working!"}