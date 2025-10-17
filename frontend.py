import streamlit as st
import requests

BACKEND_URL = "https://code-review-assistent.onrender.com"

st.title("🤖 Code Review Assistant")

st.write("Upload your Python file and get automated code review insights.")

# Upload Python file
uploaded_file = st.file_uploader("Upload Python File", type=["py"])

if uploaded_file:
    # Prepare file payload
    files = {
        "files": (uploaded_file.name, uploaded_file.getvalue(), "text/x-python")
    }
    data = {"language": "python"}

    with st.spinner("Analyzing code..."):
        try:
            response = requests.post(f"{BACKEND_URL}/review", files=files, data=data)
            result = response.json()

            st.success("✅ Review Completed")
            st.subheader("Summary")
            st.write(result["summary"])

            st.subheader("Score")
            st.progress(int(result["score"]))
            st.write(f"**{result['score']} / 100**")

            st.subheader("Suggestions")
            for s in result["suggestions"]:
                st.markdown(f"""
                - **Area:** {s.get('area', '')}  
                - **Issue:** {s.get('issue', '')}  
                - **Suggestion:** {s.get('suggestion', '')}  
                - **Snippet:**  
                  ```python
                  {s.get('snippet', '')}
                  ```
                """)

            st.subheader("Static Findings")
            st.json(result["static_findings"])

        except Exception as e:
            st.error(f"Error connecting to backend: {e}")

st.divider()

# View past reports
if st.button("📜 View All Reports"):
    try:
        reports = requests.get(f"{BACKEND_URL}/reports").json()
        if reports:
            for r in reports:
                st.markdown(f"""
                ### Report {r['id']}
                - **Score:** {r['score']}
                - **Summary:** {r['summary']}
                - **Files:** {", ".join(r['filenames'])}
                """)
        else:
            st.info("No reports found yet.")
    except Exception as e:
        st.error(f"Error fetching reports: {e}")

