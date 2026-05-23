import os

def parse_resume(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        try:
            from PyPDF2 import PdfReader
            r = PdfReader(path)
            return "\n".join((p.extract_text() or "") for p in r.pages)
        except Exception as e:
            return ""
    if ext in (".docx", ".doc"):
        try:
            import docx
            d = docx.Document(path)
            return "\n".join(p.text for p in d.paragraphs)
        except Exception:
            return ""
    # txt / fallback
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()
