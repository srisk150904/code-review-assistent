# 🚀 Code Review Assistant

An automated **code review system** that analyzes uploaded code files or pasted snippets for **readability, modularity, and potential bugs**, combining **static analysis** + **LLM suggestions**.

This project is part of a **placement evaluation** and demonstrates:

* **API design with FastAPI**
* **Static code analysis (Python AST)**
* **LLM integration (mock/real)**
* **Frontend with Streamlit**

---

## 🌐 Live Demo (No Setup Needed)

* **Frontend (Streamlit UI):**
  👉 [https://code-review-assistent-qvuhqoctvu65sxxxszt2uy.streamlit.app](https://code-review-assistent-qvuhqoctvu65sxxxszt2uy.streamlit.app)

* **Backend (FastAPI API + Docs):**
  👉 [https://code-review-assistent.onrender.com/docs](https://code-review-assistent.onrender.com/docs)

⚡ Evaluators can directly use the **Streamlit app** link. The backend is deployed separately and powers the app.

---

## 📂 Project Structure

```
code-review-assistant/
├── backend/
│   ├── app.py              # FastAPI app (main entry)
│   ├── llm.py              # LLM integration (mock/real)
│   ├── analyzers/
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
└── README.md               # Documentation
```

---

## 🔧 Local Setup (Optional)

> ⚠️ You don’t need to run locally for demo — only if you want to test/develop.

1. Clone repo & enter folder

   ```bash
   git clone <repo-url>
   cd code-review-assistant
   ```

2. Create & activate virtual environment

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run backend

   ```bash
   uvicorn backend.app:app --reload
   ```

   Visit → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

5. Run frontend

   ```bash
   streamlit run frontend.py
   ```

   Visit → [http://localhost:8501](http://localhost:8501)

---

## 🎯 How It Works

1. **Input** → Upload Python file or paste code.
2. **Static Analysis** → AST parsing detects:

   * Functions, arguments, docstrings
   * Cyclomatic complexity
   * Missing error handling, style issues
3. **LLM Suggestions** →

   * If `OPENAI_API_KEY` is set → sends findings to LLM (GPT)
   * If not → returns mock suggestions for demo
4. **Storage** → Results stored in SQLite (`reviews.db`).
5. **Output** → JSON + interactive UI with:

   * Score
   * Summary
   * Suggestions
   * Static findings

---

## ✅ Example Workflow

1. Open **Streamlit app**:
   👉 [https://code-review-assistent-qvuhqoctvu65sxxxszt2uy.streamlit.app](https://code-review-assistent-qvuhqoctvu65sxxxszt2uy.streamlit.app)

2. Upload a Python file (e.g. `examples/sample.py`).

3. Get results:

   * Score (0–100) with progress bar
   * Summary of code quality
   * Improvement suggestions
   * Static analysis findings

4. Click **View All Reports** to see history.

---

## 📌 Notes

* ✅ Works fully online (Streamlit + Render).
* ✅ No local setup needed for evaluators.
* ⚠️ On free tier, backend (Render) may “sleep” if idle; first request can take ~15 sec.
* 🧩 With `OPENAI_API_KEY`, real LLM insights can be enabled; otherwise, mock responses are shown.

---

✨ With this README, an evaluator can:

* **Directly test** the project via Streamlit link.
* **Inspect backend API** via Render link.
* Optionally, **run locally** for development.

---
