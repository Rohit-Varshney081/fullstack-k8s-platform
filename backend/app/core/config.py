from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str
    APP_ENV: str
    API_V1_PREFIX: str
    LOG_LEVEL: str = "INFO"

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

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    @property
    def DATABASE_URL(self):
        return (
            f"postgresql://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )

    @property
    def MONGO_URL(self):
        return (
            f"mongodb://{self.MONGO_HOST}:"
            f"{self.MONGO_PORT}"
        )

    @property
    def REDIS_URL(self):
        return (
            f"redis://{self.REDIS_HOST}:"
            f"{self.REDIS_PORT}/0"
        )


settings = Settings()