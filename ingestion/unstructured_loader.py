from unstructured.partition.pdf import partition_pdf

def load_pdf_unstructured(path):
    elements = partition_pdf(filename=path)

    docs = []
    for el in elements:
        text = el.text.strip() if el.text else ""
        page = getattr(el.metadata, "page_number", None)

        # skip tiny noise
        if text and len(text) > 80:
            docs.append({
                "text": text,
                "page": page
            })

    return docs
