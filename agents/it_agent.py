from tools.retriever import retrieve_docs
from tools.intent_classifier import classify_intent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
RELEVANCE_THRESHOLD = 0.9

def it_agent(query):
    intent = classify_intent("IT", query)

    if intent["type"] == "action":
        return intent

    context = retrieve_docs(query)

    if not context["content"]:
        return {"type": "knowledge", "answer": "Not mentioned in IT documents.", "citations": []}

    best_score = context["scores"][0]
    print("IT Top similarity score:", best_score)

    if best_score > RELEVANCE_THRESHOLD:
        return {"type": "knowledge", "answer": "Not mentioned in IT documents.", "citations": []}

    combined = "\n\n".join(context["content"][:3])

    prompt = f"""
Answer strictly from the IT documentation.
If not present say: Not mentioned in the document.

Context:
{combined}

Question:
{query}
"""

    answer = llm.invoke(prompt).content.strip()

    if "not mentioned" in answer.lower():
        return {"type": "knowledge", "answer": "Not mentioned in IT documents.", "citations": []}

    return {
        "type": "knowledge",
        "answer": answer,
        "citations": context["pages"][:3]
    }
