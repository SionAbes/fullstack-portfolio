from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):

    ENV: str
    MASTER_API_BASE: str
    MASTER_API_USERNAME: str
    MASTER_API_PASSWORD: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings(_env_file=".env")
