Got it ✅ Since this project is part of your **placement evaluation**, I’ll make the `README.md` very clear, step-by-step, so anyone (even without prior setup) can run and test it quickly.

Here’s a polished `README.md` you can drop into your repo:

---

# 🚀 Code Review Assistant

An automated **code review system** that analyzes uploaded code files or pasted snippets for **readability, modularity, and potential bugs**, combining **static analysis** + **LLM suggestions**.

This project is designed to showcase **API design, code analysis, and LLM integration**.

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
├── requirements.txt        # Python dependencies
├── .env.example            # Environment template
└── README.md               # Documentation
```

---

## ⚡ Requirements

* **Python 3.10+**
* **pip** (Python package manager)
* (Optional) **OpenAI API key** for real LLM reviews.
  *(By default, a mock reviewer is used so it works offline too.)*

---

## 🔧 Setup

1. **Clone repo & enter project folder**

   ```bash
   git clone <repo-url>
   cd code-review-assistant
   ```

2. **Create virtual environment**

   ```bash
   python -m venv .venv
   ```

3. **Activate venv**

   * Windows (PowerShell):

     ```bash
     .venv\Scripts\activate
     ```
   * Linux/Mac:

     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Setup environment file**

   ```bash
   copy .env.example .env   # Windows
   # OR
   cp .env.example .env     # Linux/Mac
   ```

   Edit `.env` if you want to add:

   ```
   OPENAI_API_KEY=sk-xxxx
   DB_URL=sqlite:///./reviews.db
   ```

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn backend.app:app --reload
```

Expected output:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## 🌐 Using the API

### 📘 1. Open Docs

Visit: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**
This opens **Swagger UI**, where you can try endpoints interactively.

---

### 📝 2. Endpoints

#### **POST /review** → Review uploaded code

Options:

* Upload file(s) (e.g. `examples/sample.py`)
* OR paste code snippets in `text_parts`
* OR do both

Example (file upload):

```bash
curl -X POST "http://127.0.0.1:8000/review" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "language=python" \
  -F "files=@examples/sample.py;type=text/x-python"
```

Example (text snippet):

```bash
curl -X POST "http://127.0.0.1:8000/review" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "language=python" \
  -F "text_parts=def add(a, b):\n    return a+b"
```

Response:

```json
{
  "id": 1,
  "score": 78,
  "summary": "Overall OK structure; consider splitting large functions and adding docstrings.",
  "suggestions": [
    {
      "area": "readability",
      "issue": "Long function without docstring",
      "suggestion": "Add a docstring and split into helpers.",
      "snippet": "def processData(...): ..."
    }
  ],
  "static_findings": {
    "per_file": [
      {
        "filename": "sample.py",
        "findings": { "line_count": 31, "functions": [...] }
      }
    ]
  },
  "filenames": ["sample.py"]
}
```

---

#### **GET /reports** → List all past reviews

```bash
curl -X GET "http://127.0.0.1:8000/reports"
```

---

#### **GET /reports/{id}** → Fetch one review by ID

```bash
curl -X GET "http://127.0.0.1:8000/reports/1"
```

---

## 🔍 How it Works

1. **Input**: Source code (via file or text)
2. **Static Analysis**:

   * Python AST parsing (functions, docstrings, complexity, style issues)
   * Counts lines, detects long functions, missing docstrings, bad practices
3. **LLM Integration**:

   * (If API key present) → sends code + static findings to LLM for deeper review
   * (If no key) → uses a mock reviewer that returns example suggestions
4. **Storage**:

   * Review results saved into SQLite (`reviews.db`)
5. **Output**: JSON report with `score`, `summary`, `suggestions`, and static findings

---

## 🎯 Demo Flow

1. Run server with `uvicorn backend.app:app --reload`
2. Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
3. Try **POST /review** → upload `examples/sample.py`
4. View JSON response → shows score + suggestions
5. Try **GET /reports** → see history of reviews

---

## ✅ Example Output

```json
{
  "id": 1,
  "score": 78,
  "summary": "Overall OK structure; consider splitting large functions and adding docstrings.",
  "suggestions": [
    { "area": "readability", "issue": "No docstring in function", "suggestion": "Add docstring" }
  ],
  "filenames": ["sample.py"]
}
```

---

## 📌 Notes

* Works offline with mock suggestions.
* Add your `OPENAI_API_KEY` in `.env` for real LLM insights.
* Database is auto-created as `reviews.db` in project folder.

---

✨ With this README, an evaluator can:

* Set up the venv
* Install deps
* Run the server
* Test via Swagger or `curl`
* Clearly understand how code → review report works

---

Would you like me to also write a **1–2 minute demo script** (like what to show on screen, what to say) so you can record your demo video smoothly?
