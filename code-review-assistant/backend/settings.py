from pydantic import BaseModel
import os

class Settings(BaseModel):
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
    DB_URL: str = os.getenv("DB_URL", "sqlite:///./reviews.db")
    MODEL: str = os.getenv("MODEL", "gpt-4o-mini")  # or your provider
    MAX_FILE_SIZE_MB: int = int(os.getenv("MAX_FILE_SIZE_MB", "2"))

settings = Settings()
