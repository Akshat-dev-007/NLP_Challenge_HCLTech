def chunk_docs(docs, chunk_size=800, overlap=100):
    chunks = []

    for doc in docs:
        text = doc["text"]
        page = doc["page"]

        for i in range(0, len(text), chunk_size - overlap):
            chunks.append({
                "content": text[i:i + chunk_size],
                "page": page
            })

    return chunks
