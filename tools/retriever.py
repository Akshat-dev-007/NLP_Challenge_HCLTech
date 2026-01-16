from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def retrieve_docs(query, k=8, fetch_k=25, lambda_mult=0.6):
    """
    MMR retrieval + correct semantic scoring.
    Lower score = more relevant.
    """
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    db = Chroma(
        persist_directory="vector_store/chroma_db",
        embedding_function=embeddings
    )

    # Step 1: Get diverse docs using MMR
    mmr_docs = db.max_marginal_relevance_search(
        query=query,
        k=k,
        fetch_k=fetch_k,
        lambda_mult=lambda_mult
    )

    # Step 2: Properly score them against the USER QUERY
    rescored = []
    for doc in mmr_docs:
        # We compute similarity of (query ↔ doc)
        results = db.similarity_search_with_score(query, k=1)
        score = results[0][1]
        rescored.append((doc, score))

    # Step 3: Sort by best match
    rescored = sorted(rescored, key=lambda x: x[1])

    return {
        "content": [doc.page_content for doc, _ in rescored],
        "pages": [doc.metadata.get("page") for doc, _ in rescored],
        "scores": [score for _, score in rescored]
    }
