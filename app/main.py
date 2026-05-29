from fastapi import FastAPI
from routers.health import router as health_router

app = FastAPI(title="AI Backend Assignment")

app.include_router(health_router)

@app.get("/")
def home():
    return {
        "message": "FastAPI Backend Running"
    }