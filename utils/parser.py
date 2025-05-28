# utils/parser.py

import os
import fitz  # PyMuPDF
import docx
import io
# Retourne une chaîne de texte propre à partir du fichier uploadé via Streamlit
def extract_text(uploaded_file):
    ext = os.path.splitext(uploaded_file.name)[-1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf(uploaded_file)
    elif ext == ".docx":
        return extract_text_from_docx(uploaded_file)
    elif ext == ".txt":
        return uploaded_file.read().decode("utf-8")
    else:
        return "Format non pris en charge"

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(file):
    text = ""
    doc = docx.Document(io.BytesIO(file.read()))
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text
