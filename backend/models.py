from datetime import datetime
from typing import Optional, Dict, Any
from sqlmodel import SQLModel, Field, create_engine, Session
from sqlalchemy import Column
from sqlalchemy.dialects.sqlite import JSON  # JSON column type for lists/dicts


class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    language: str

    filenames: list[str] = Field(sa_column=Column(JSON))         # store list
    static_findings: Dict[str, Any] = Field(sa_column=Column(JSON))  # store dict
    llm_summary: str
    llm_suggestions: list[dict] = Field(sa_column=Column(JSON))  # store list of dicts
    score: float


def get_engine(db_url: str):
    return create_engine(db_url, echo=False)


def init_db(engine):
    SQLModel.metadata.create_all(engine)


def get_session(engine):
    return Session(engine)
