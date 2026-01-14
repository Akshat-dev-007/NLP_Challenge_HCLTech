def chunk_docs(docs, chunk_size=1000, overlap=200):
    chunks = []
    for doc in docs:
        text = doc["text"]
        for i in range(0, len(text), chunk_size - overlap):
            chunks.append({
                "content": text[i:i+chunk_size],
                "page": doc["page"]
            })
    return chunks
