from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV: str = "local"

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings(_env_file="../.env")
