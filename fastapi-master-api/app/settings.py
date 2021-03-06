from typing import Any, Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    ENV: str
    BOOTSTRAP_SERVER: str
    HASH_SECRET: str
    JWT_SECRET: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str
    SQLALCHEMY_MAX_CONNECTIONS: int = 2
    API_URL: str
    SQL_HOST: str
    SQL_PORT: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    SQLALCHEMY_DATABASE_URL: Optional[PostgresDsn] = None
    SKIP_SESSION_HANDLER: bool = False

    @validator("SQLALCHEMY_DATABASE_URL", pre=True)
    def assemble_db_connection(
        cls, sqlalchemy_database_url: Optional[str], values: Dict[str, Any]
    ) -> Any:
        if isinstance(sqlalchemy_database_url, str):
            return sqlalchemy_database_url
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("SQL_HOST"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
            port=f"{values.get('SQL_PORT') or '5432'}",
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def get_settings() -> Settings:
    return Settings(_env_file=".env")
