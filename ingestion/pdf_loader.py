from pypdf import PdfReader

def load_pdf(path):
    reader = PdfReader(path)
    docs = []
    for i, page in enumerate(reader.pages):
        docs.append({
            "text": page.extract_text(),
            "page": i + 1
        })
    return docs
