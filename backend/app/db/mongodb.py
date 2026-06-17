from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings

client = AsyncIOMotorClient(
    f"mongodb://{settings.MONGO_HOST}:{settings.MONGO_PORT}"
)

database = client[settings.MONGO_DB]