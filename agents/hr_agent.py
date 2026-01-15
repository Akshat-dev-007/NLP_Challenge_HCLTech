from tools.retriever import retrieve_docs

def hr_agent(query):
    q = query.lower()

    # ---- ACTION INTENTS ----

    # 1. Leave application
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

    # 2. Schedule meeting with HR
    if "schedule" in q and "meeting" in q:
        return {
            "type": "action",
            "function": "schedule_meeting",
            "arguments": {
                "department": "HR",
                "title": "HR Discussion",
                "date": "to_be_decided",
                "time": "to_be_decided"
            }
        }

    # ---- KNOWLEDGE INTENT (RAG) ----
    context = retrieve_docs(query)

    if not context["content"]:
        return {
            "type": "knowledge",
            "answer": "No relevant HR policy found in the document.",
            "citations": []
        }

    combined_context = "\n".join(context["content"][:3])

    return {
        "type": "knowledge",
        "answer": f"Based on HR policy documents: {combined_context[:700]}...",
        "citations": context["pages"]
    }

