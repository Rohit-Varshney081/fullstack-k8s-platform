from fastapi import FastAPI

from app.api.health import router as health_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FullStack Platform API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Application Running"
    }