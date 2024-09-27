import os
import pdfplumber
from config import PDF_FOLDER, TEXT_FOLDER

def find_textile_info(query):
    """Searches through PDFs and text files for textile-related information."""
    # Search through PDF files
    for pdf_file in os.listdir(PDF_FOLDER):
        if pdf_file.endswith('.pdf'):
            with pdfplumber.open(os.path.join(PDF_FOLDER, pdf_file)) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text and query.lower() in text.lower():
                        return f"PDF result: {text}"

    # Search through text files
    for text_file in os.listdir(TEXT_FOLDER):
        if text_file.endswith('.txt'):
            with open(os.path.join(TEXT_FOLDER, text_file), 'r', encoding='utf-8') as file:
                text = file.read()
                if query.lower() in text.lower():
                    return f"Text result: {text}"

    return None
