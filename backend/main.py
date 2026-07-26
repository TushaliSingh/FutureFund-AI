from fastapi import FastAPI

from backend.api.v1.router import api_router

app = FastAPI(
    title="FutureFund AI API",
    description="Backend API for the FutureFund AI Investment Platform",
    version="1.0.0",
)

app.include_router(
    api_router,
    prefix="/api/v1",
    tags=["API v1"],
)


@app.get("/")
def root():
    return {
        "message": "Welcome to FutureFund AI Backend!",
        "status": "running",
        "version": "1.0.0",
    }