from tools.retriever import retrieve_docs

def dev_agent(query):
    q = query.lower()

    # (Optional) Action intent later: build, deploy, create repo, etc.
    # For now dev agent is knowledge-only

    context = retrieve_docs(query)

    # SAFE CHECK
    if not context["content"]:
        return {
            "type": "knowledge",
            "answer": "No developer documentation found in the knowledge base. Please upload or ingest developer docs.",
            "citations": []
        }

    # Combine multiple chunks for better answers
    combined_context = "\n".join(context["content"][:2])

    return {
        "type": "knowledge",
        "answer": f"From developer documentation: {combined_context[:500]}...",
        "citations": context["pages"]
    }
