from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class ReviewRequest(BaseModel):
    language: str = Field(..., description="e.g., python, js")
    text_parts: List[str] | None = None  # optional for raw text body submissions

class ReviewResponse(BaseModel):
    id: int
    score: float
    summary: str
    suggestions: List[Dict]
    static_findings: Dict
    filenames: List[str]
