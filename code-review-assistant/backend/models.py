from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, JSON, create_engine, Session

class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    language: str
    filenames: List[str] = Field(sa_column=JSON)
    static_findings: dict = Field(sa_column=JSON)
    llm_summary: str
    llm_suggestions: List[dict] = Field(sa_column=JSON)  # [{area, issue, suggestion, snippet}]
    score: float

def get_engine(db_url: str):
    return create_engine(db_url, echo=False)

def init_db(engine):
    SQLModel.metadata.create_all(engine)

def get_session(engine):
    return Session(engine)
