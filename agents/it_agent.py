# agents/it_agent.py
from tools.retriever import retrieve_docs

def it_agent(query):
    q = query.lower()

    # Action intent → ticket creation
    if "ticket" in q or "raise" in q:
        return {
            "type": "action",
            "function": "create_ticket",
            "arguments": {
                "issue": query,
                "priority": "High"
            }
        }

    # Knowledge intent → RAG
    context = retrieve_docs(query)

    # SAFE CHECK (this is what prevents IndexError)
    if not context["content"]:
        return {
            "type": "knowledge",
            "answer": "No IT troubleshooting documentation found in the knowledge base. Please try raising a ticket.",
            "citations": []
        }

    combined_context = "\n".join(context["content"][:2])

    return {
        "type": "knowledge",
        "answer": f"Suggested troubleshooting based on IT documentation: {combined_context[:500]}...",
        "citations": context["pages"]
    }
