# utils/file_utils.py
import json
from PyPDF2 import PdfReader

def extract_text_from_pdf(file) -> str:
    reader = PdfReader(file)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def extract_text_from_json(file) -> str:
    data = json.load(file)
    return json.dumps(data, indent=2)  # Flatten for embedding

def split_text_into_chunks(text: str, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
