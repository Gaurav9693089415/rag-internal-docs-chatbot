from pypdf import PdfReader

def load_pdf(file_path):
    reader = PdfReader(file_path)
    text = " ".join(page.extract_text() for page in reader.pages)
    return text
