from fastapi import FastAPI

from app.api.health import router as health_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.users import router as user_router

app = FastAPI(
    title="FullStack Platform API"
)
# from app.db.base import Base
# from app.db.postgres import engine

# Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(health_router)

app.include_router(user_router)

@app.get("/")
def root():
    return {
        "message": "Application Running"
    }