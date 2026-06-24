from fastapi import FastAPI

from app.api.health import router as health_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.users import router as user_router
from app.api.auth import router as auth_router
from app.api.tasks import router as task_router
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/api/openapi.json",
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
Instrumentator().instrument(app).expose(app)


app.include_router(health_router)
app.include_router(task_router)

app.include_router(auth_router)
app.include_router(user_router)


@app.get("/")
def root():
    return {
        "message": "Application Running"
    }