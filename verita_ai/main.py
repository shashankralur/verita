from fastapi import FastAPI

app = FastAPI(title="Verita AI")

@app.get("/")
def home():
    return {
        "message": "Welcome to Verita AI API"
    }