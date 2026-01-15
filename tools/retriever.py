from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def retrieve_docs(query):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    db = Chroma(
        persist_directory="vector_store/chroma_db",
        embedding_function=embeddings
    )

    docs = db.max_marginal_relevance_search(
        query,
        k=5,
        fetch_k=20,
        lambda_mult=0.6
    )

    return {
        "content": [d.page_content for d in docs],
        "pages": [d.metadata.get("page") for d in docs]
    }
