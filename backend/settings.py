from pydantic import BaseModel
import os

class Settings(BaseModel):
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")

    _db_url = os.getenv("DB_URL", "").strip()
    # Use SQLite fallback if invalid/empty
    DB_URL: str = _db_url if _db_url.startswith("sqlite:") else "sqlite:///./reviews.db"

    MODEL: str = os.getenv("MODEL", "gpt-4o-mini")
    MAX_FILE_SIZE_MB: int = int(os.getenv("MAX_FILE_SIZE_MB", "2"))

settings = Settings()
