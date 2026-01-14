from tools.retriever import retrieve_docs

def hr_agent(query):
    q = query.lower()

    # Action intent
    if "apply" in q and "leave" in q:
        return {
            "type": "action",
            "function": "apply_leave",
            "arguments": {
                "leave_type": "Casual",
                "days": 2,
                "start_date": "tomorrow"
            }
        }

    # Knowledge intent
    enhanced_query = f"Casual leave policy entitlement number of days HR policy {query}"
    context = retrieve_docs(enhanced_query)

    #context = retrieve_docs(query)

    if not context["content"]:
        return {
            "type": "knowledge",
            "answer": "No relevant HR policy found in the knowledge base.",
            "citations": []
        }

    combined_context = "\n".join(context["content"][:3])

    return {
        "type": "knowledge",
        "answer": f"Based on HR policy documents: {combined_context[:700]}...",
        "citations": context["pages"]
    }
