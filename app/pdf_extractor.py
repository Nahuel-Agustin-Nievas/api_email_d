from PyPDF2 import PdfReader
import io

def extract_first_30_lines(pdf_content: bytes) -> str:
    reader = PdfReader(io.BytesIO(pdf_content))
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        if len(text.splitlines()) >= 30:
            break
    
    lines = text.splitlines()[:30]
    return "\n".join(lines)
