from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router


app = FastAPI(
    title="NIVARA API",
    description="AI-Powered Healthcare Journey Intelligence",
    version="0.1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    router,
    prefix="/api",
    tags=["Journey Simulation"]
)


@app.get("/")
def root():
    return {
        "message": "NIVARA API is running",
        "version": "0.1.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "NIVARA"
    }