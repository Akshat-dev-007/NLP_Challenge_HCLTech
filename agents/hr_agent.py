from tools.retriever import retrieve_docs
from tools.intent_classifier import classify_intent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
RELEVANCE_THRESHOLD = 0.9

def hr_agent(query):
    intent = classify_intent("HR", query)

    # ACTION MODE
    if intent["type"] == "action":
        return intent

    # KNOWLEDGE MODE (RAG)
    context = retrieve_docs(query)

    if not context["content"]:
        return {"type": "knowledge", "answer": "Not mentioned in the document.", "citations": []}

    best_score = context["scores"][0]
    print("HR Top similarity score:", best_score)

    if best_score > RELEVANCE_THRESHOLD:
        return {"type": "knowledge", "answer": "Not mentioned in the document.", "citations": []}

    combined = "\n\n".join(context["content"][:3])

    prompt = f"""
Answer strictly using the context below.
If the answer is not present say: "Not mentioned in the document."

Context:
{combined}

Question:
{query}
"""
    answer = llm.invoke(prompt).content.strip()

    if "not mentioned" in answer.lower():
        return {"type": "knowledge", "answer": "Not mentioned in the document.", "citations": []}

    return {
        "type": "knowledge",
        "answer": answer,
        "citations": context["pages"][:3]
    }
