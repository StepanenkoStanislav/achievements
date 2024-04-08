import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent.parent

load_dotenv(BASE_DIR / ".env")


class DbSettings(BaseModel):
    """Настройки для БД."""

    postgres_db: str = os.getenv("POSTGRES_DB", "achievements")
    postgres_user: str = os.getenv("DB_USER", "achievements_admin")
    postgres_password: str = os.getenv("DB_PASSWORD", "password")
    postgres_host: str = os.getenv("DB_HOST", "db")
    postgres_port: str = os.getenv("DB_PORT", "5432")
    db_url: str = (
        f"postgresql+asyncpg://{postgres_user}:{postgres_password}"
        f"@{postgres_host}:{postgres_port}/{postgres_db}"
    )


class Settings(BaseSettings):
    """Настройки проекта."""

    app_title: str = "Achievements"
    app_description: str = "API для работы с достижениями"

    api_v1_prefix: str = "/api/v1"

    db: DbSettings = DbSettings()


settings = Settings()
