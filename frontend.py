import streamlit as st
import requests

# Backend URL (your deployed FastAPI service on Render)
BACKEND_URL = "https://code-review-assistent.onrender.com"

st.set_page_config(page_title="Code Review Assistant", page_icon="🤖", layout="wide")

st.title("🤖 Code Review Assistant")
st.write("Upload your Python file and get automated code review insights.")

# --- File Upload ---
uploaded_file = st.file_uploader("📂 Upload Python File", type=["py"])

if uploaded_file:
    files = {
        "files": (uploaded_file.name, uploaded_file.getvalue(), "text/x-python")
    }
    data = {"language": "python"}

    with st.spinner("🔍 Analyzing your code..."):
        try:
            response = requests.post(f"{BACKEND_URL}/review", files=files, data=data)
            response.raise_for_status()
            result = response.json()

            # --- Results ---
            st.success("✅ Review Completed")

            st.subheader("📌 Summary")
            st.write(result.get("summary", "No summary available."))

            st.subheader("📊 Score")
            score = int(result.get("score", 0))
            st.progress(score)
            st.write(f"**{score} / 100**")

            st.subheader("💡 Suggestions")
            if result.get("suggestions"):
                for s in result["suggestions"]:
                    st.markdown(f"""
                    - **Area:** {s.get('area', 'N/A')}  
                    - **Issue:** {s.get('issue', 'N/A')}  
                    - **Suggestion:** {s.get('suggestion', 'N/A')}  
                    - **Snippet:**  
                      ```python
                      {s.get('snippet', '')}
                      ```
                    """)
            else:
                st.info("No suggestions provided.")

            st.subheader("📑 Static Findings")
            st.json(result.get("static_findings", {}))

        except Exception as e:
            st.error(f"❌ Error connecting to backend: {e}")

st.divider()

# --- Reports Section ---
st.subheader("📜 Past Reports")
if st.button("🔄 Refresh Reports"):
    try:
        reports = requests.get(f"{BACKEND_URL}/reports").json()
        if reports:
            for r in reports:
                with st.expander(f"📄 Report {r['id']} - Score {r['score']}"):
                    st.markdown(f"""
                    - **Summary:** {r['summary']}  
                    - **Files:** {", ".join(r['filenames'])}
                    """)
        else:
            st.info("No reports found yet.")
    except Exception as e:
        st.error(f"❌ Error fetching reports: {e}")
