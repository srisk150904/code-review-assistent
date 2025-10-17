from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select
from typing import List
from settings import settings
from models import Review, get_engine, init_db, get_session
from schemas import ReviewResponse
from analyzers.python_static import analyze_python
from llm import review_with_llm
from utils import read_files

app = FastAPI(title="Code Review Assistant", version="0.1.0")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

engine = get_engine(settings.DB_URL)
init_db(engine)

@app.post("/review", response_model=ReviewResponse)
async def review_endpoint(
    language: str = Form(...),
    files: List[UploadFile] = File(default=[]),
    text_parts: List[str] = Form(default=None)
):
    if not files and not text_parts:
        raise HTTPException(status_code=400, detail="Provide at least one file or text_parts.")

    in_files = await read_files(files) if files else []
    if text_parts:
        for i, t in enumerate(text_parts):
            in_files.append({"filename": f"text_{i+1}.txt", "content": t})

    # Basic language switch; extend with more analyzers
    static_findings = {}
    if language.lower() == "python":
        # Merge all sources for a module-level view + per-file stats
        per_file = []
        for f in in_files:
            per_file.append({"filename": f["filename"], "findings": analyze_python(f["content"])})
        static_findings["per_file"] = per_file
    else:
        static_findings["note"] = f"No static analyzer implemented for '{language}', LLM-only review."

    llm_result = review_with_llm(language, in_files, static_findings)

    with get_session(engine) as session:
        review = Review(
            language=language.lower(),
            filenames=[f["filename"] for f in in_files],
            static_findings=static_findings,
            llm_summary=llm_result["summary"],
            llm_suggestions=llm_result.get("suggestions", []),
            score=float(llm_result.get("score", 0.0)),
        )
        session.add(review)
        session.commit()
        session.refresh(review)

        return ReviewResponse(
            id=review.id,
            score=review.score,
            summary=review.llm_summary,
            suggestions=review.llm_suggestions,
            static_findings=review.static_findings,
            filenames=review.filenames,
        )

@app.get("/reports", response_model=list[ReviewResponse])
def list_reports(limit: int = 25, offset: int = 0):
    with get_session(engine) as session:
        rows = session.exec(select(Review).order_by(Review.created_at.desc()).offset(offset).limit(limit)).all()
        return [
            ReviewResponse(
                id=r.id, score=r.score, summary=r.llm_summary,
                suggestions=r.llm_suggestions, static_findings=r.static_findings, filenames=r.filenames
            ) for r in rows
        ]

@app.get("/reports/{report_id}", response_model=ReviewResponse)
def get_report(report_id: int):
    with get_session(engine) as session:
        r = session.get(Review, report_id)
        if not r:
            raise HTTPException(status_code=404, detail="Not found")
        return ReviewResponse(
            id=r.id, score=r.score, summary=r.llm_summary,
            suggestions=r.llm_suggestions, static_findings=r.static_findings, filenames=r.filenames
        )
