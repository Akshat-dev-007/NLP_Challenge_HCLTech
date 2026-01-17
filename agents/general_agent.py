from tools.retriever import retrieve_docs
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Finance PDFs need higher threshold
RELEVANCE_THRESHOLD = 1.3  

def general_agent(query):
    context = retrieve_docs(query, k=8)

    if not context["content"]:
        return {
            "type": "knowledge",
            "answer": "Not mentioned in the document.",
            "citations": []
        }

    best_score = context["scores"][0]
    print("GENERAL Top similarity score:", best_score)

    # Reject only if similarity is very weak
    if best_score > RELEVANCE_THRESHOLD:
        return {
            "type": "knowledge",
            "answer": "Not mentioned in the document.",
            "citations": []
        }

    combined = "\n\n".join(context["content"][:4])

    prompt = f"""
Extract the factual answer from the context.
Do NOT return JSON.
Do NOT say "not mentioned" if information exists.

Context:
{combined}

Question:
{query}

Answer in plain English:
"""

    answer = llm.invoke(prompt).content.strip()

    # Final safety: never attach citations to a refusal
    if "not mentioned" in answer.lower() or "not provide" in answer.lower():
        return {
            "type": "knowledge",
            "answer": "Not mentioned in the document.",
            "citations": []
        }

    return {
        "type": "knowledge",
        "answer": answer,
        "citations": context["pages"][:3]
    }
