from typing import Dict, Any, List
from tenacity import retry, stop_after_attempt, wait_exponential
from settings import settings
import os

# If using OpenAI:
# from openai import OpenAI
# client = OpenAI(api_key=settings.OPENAI_API_KEY)

SYSTEM_PROMPT = """You are a senior code reviewer.
Return JSON with keys: summary (string), score (0-100), suggestions (list of {area, issue, suggestion, snippet}).
Emphasize: readability, modularity, potential bugs, testability, security.
Be concise and actionable.
"""

def build_user_prompt(language: str, files: List[Dict[str, str]], static_findings: Dict[str, Any]) -> str:
    parts = [f"Language: {language}", "Static findings:"]
    parts.append(str(static_findings))
    parts.append("Files:")
    for f in files:
        parts.append(f"--- {f['filename']} ---\n{f['content']}")
    return "\n\n".join(parts)

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=1, max=8))
def review_with_llm(language: str, files: List[Dict[str, str]], static_findings: Dict[str, Any]) -> Dict[str, Any]:
    # Pseudo-call — plug your provider here. Return structured dict.
    # Example with OpenAI (uncomment to use):
    """
    prompt = build_user_prompt(language, files, static_findings)
    resp = client.chat.completions.create(
        model=settings.MODEL,
        messages=[{"role":"system","content":SYSTEM_PROMPT},
                  {"role":"user","content":prompt}],
        temperature=0.2,
        response_format={"type":"json_object"}
    )
    return json.loads(resp.choices[0].message.content)
    """
    # Fallback deterministic mock (useful for local dev without keys)
    return {
        "summary": "Overall OK structure; consider splitting large functions and adding docstrings.",
        "score": 78.0,
        "suggestions": [
            {"area": "readability", "issue": "Long function without docstring", "suggestion": "Add a docstring and split into helpers.", "snippet": "def process_data(...): ..."},
            {"area": "bugs", "issue": "No error handling around file IO", "suggestion": "Wrap with try/except and log errors.", "snippet": "with open(path) as f: ..."},
        ],
    }
