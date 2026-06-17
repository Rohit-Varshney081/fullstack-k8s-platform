from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    APP_ENV: str

    API_V1_PREFIX: str

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    MONGO_HOST: str
    MONGO_PORT: int
    MONGO_DB: str

    REDIS_HOST: str
    REDIS_PORT: int

    LOG_LEVEL: str
    
    DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:"
    f"{POSTGRES_PASSWORD}@"
    f"{POSTGRES_HOST}:"
    f"{POSTGRES_PORT}/"
    f"{POSTGRES_DB}"
    )

    MONGO_URL = (
        f"mongodb://{MONGO_HOST}:{MONGO_PORT}"
    )

    REDIS_URL = (
        f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
    )

    class Config:
        env_file = ".env"


settings = Settings()