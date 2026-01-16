from tools.retriever import retrieve_docs
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
RELEVANCE_THRESHOLD = 1.1  # looser for GENERAL

def general_agent(query):
    context = retrieve_docs(query)

    if not context["content"]:
        return {
            "type": "knowledge",
            "answer": "Not mentioned in the document.",
            "citations": []
        }

    best_score = context["scores"][0]
    print("GENERAL Top similarity score:", best_score)

    # Hard reject only if retrieval is truly weak
    if best_score > RELEVANCE_THRESHOLD:
        return {
            "type": "knowledge",
            "answer": "Not mentioned in the document.",
            "citations": []
        }

    combined = "\n\n".join(context["content"][:4])

    prompt = f"""
You are answering using a company annual report.

The context DEFINITELY contains relevant information.
Do NOT say that information is missing if the context talks about the topic.

Extract the factual answer directly from the context.

Context:
{combined}

Question:
{query}

Answer:
"""

    answer = llm.invoke(prompt).content.strip()

    # Final citation gate: if model still says "not mentioned", drop citations
    if "not provide" in answer.lower() or "not mentioned" in answer.lower():
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
