# 🚀 Code Review Assistant

An automated **code review system** that analyzes uploaded code files or pasted snippets for **readability, modularity, and potential bugs**, combining **static analysis** + **LLM suggestions**.

This project is designed to showcase **API design, code analysis, LLM integration, and a working frontend**.

---

## 🌐 Live Demo

👉 **Frontend (Streamlit UI):**
🔗 [https://your-streamlit-app.streamlit.app]([https://your-streamlit-app.streamlit.app](https://code-review-assistent-qvuhqoctvu65sxxxszt2uy.streamlit.app/))

👉 **Backend (FastAPI API Docs):**
🔗 [https://code-review-assistent.onrender.com/docs](https://code-review-assistent.onrender.com/docs)

*(For evaluators: You can directly use the Streamlit app above. The backend API is deployed separately on Render and powers the UI.)*

---

## 📂 Project Structure

```
code-review-assistant/
├── backend/
│   ├── app.py              # FastAPI app (main entry)
│   ├── llm.py              # LLM integration (mock/real)
│   ├── analyzers/
│   │   ├── __init__.py
│   │   └── python_static.py # Python AST static analyzer
│   ├── models.py           # SQLModel schema + DB helpers
│   ├── schemas.py          # Request/response schemas
│   ├── settings.py         # Config & environment variables
│   └── utils.py            # File handling utilities
├── examples/
│   └── sample.py           # Example test file
├── tests/
│   └── test_api_smoke.py   # Simple test scaffold
├── frontend.py             # Streamlit UI
├── requirements.txt        # Python dependencies
├── .env.example            # Environment template
└── README.md               # Documentation
```

---

## ⚡ Requirements (for local run)

* **Python 3.10+**
* **pip**
* (Optional) **OpenAI API key** for real LLM reviews
  *(By default, a mock reviewer is used so it works offline too.)*

---

## ▶️ Running Locally

### 1. Backend (FastAPI)

Start backend API:

```bash
uvicorn backend.app:app --reload
```

Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 2. Frontend (Streamlit)

Run frontend:

```bash
streamlit run frontend.py
```

UI → [http://localhost:8501](http://localhost:8501)

---

## 🎯 How It Works

1. **Input**: Upload Python file or paste code snippet.
2. **Static Analysis**:

   * Parses code using AST
   * Finds missing docstrings, large functions, cyclomatic complexity, style issues
3. **LLM Suggestions**:

   * If `OPENAI_API_KEY` is provided → sends code + findings to LLM
   * Else → returns mock suggestions for demo
4. **Storage**:

   * Results stored in SQLite (`reviews.db`)
5. **Output**: JSON + Streamlit dashboard with:

   * Score
   * Summary
   * Suggestions
   * Static findings

---

## ✅ Example Workflow

1. Open the **Streamlit app**:
   👉 [https://your-streamlit-app.streamlit.app](https://your-streamlit-app.streamlit.app)

2. Upload `examples/sample.py`.

3. Get:

   * Score (0–100) with progress bar
   * Readability/bug/modularity suggestions
   * Static analysis findings

4. View past reports in the UI.

---

## 📌 Notes

* Works offline with mock suggestions.
* Add your `OPENAI_API_KEY` in `.env` for real LLM integration.
* Backend is deployed on Render (ephemeral SQLite DB).
* Frontend is deployed on Streamlit Cloud for easy access.

---

✨ With this setup, an evaluator can:

* Use the **live Streamlit demo** directly
* Or run backend + frontend locally
* Clearly see how uploaded code → review report pipeline works

---
