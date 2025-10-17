from typing import List, Dict
from fastapi import UploadFile

async def read_files(files: List[UploadFile]) -> List[Dict[str, str]]:
    out = []
    for f in files:
        content = (await f.read()).decode("utf-8", errors="replace")
        out.append({"filename": f.filename, "content": content})
    return out
