from fastapi import FastAPI
from src.router.chat import router as chat_router

app = FastAPI(
    title="Verita AI API"
)

print("Loaded Verita AI API")

# Register chat routes
app.include_router(chat_router)

@app.get("/")
def home():
    return {"message": "Welcome to Verita AI"}