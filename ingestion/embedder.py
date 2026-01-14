from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    return Chroma.from_texts(
        texts=[c["content"] for c in chunks],
        metadatas=[{"page": c["page"]} for c in chunks],
        embedding=embeddings,
        persist_directory="vectorstore/chroma_db"
    )
