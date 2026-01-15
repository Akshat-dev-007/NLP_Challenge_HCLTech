from tools.retriever import retrieve_docs
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def general_agent(query):
    context = retrieve_docs(query)

    if not context["content"]:
        return {
            "type": "knowledge",
            "answer": "No relevant information found in the PDF.",
            "citations": []
        }

    combined_context = "\n".join(context["content"][:4])

    prompt = f"""
You are a helpful assistant answering strictly from the provided document.

Context:
{combined_context}

Question:
{query}

Answer clearly and concisely. If not found, say "Not mentioned in the document".
"""

    response = llm.invoke(prompt).content

    return {
        "type": "knowledge",
        "answer": response,
        "citations": context["pages"]
    }
