from ingestion.unstructured_loader import load_pdf_unstructured
from ingestion.chunking import chunk_docs
from ingestion.embedder import create_vectorstore
import shutil
import os

PDF_PATH = "Annual-Report-2024-25.pdf"
VECTOR_DIR = "vector_store/chroma_db"

# Delete old DB
if os.path.exists(VECTOR_DIR):
    shutil.rmtree(VECTOR_DIR)
    print("Old vector store deleted")

# Load using Unstructured
docs = load_pdf_unstructured(PDF_PATH)
print("Semantic blocks:", len(docs))

# Chunk
chunks = chunk_docs(docs)
print("Chunks created:", len(chunks))

# Embed
create_vectorstore(chunks)
print("New vector DB built using Unstructured + semantic chunking")
