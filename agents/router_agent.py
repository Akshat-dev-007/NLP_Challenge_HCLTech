from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
import json

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def route_query(query: str):
    prompt = f"""
You are a router for a multi-agent AI assistant.

Decide which domain should handle the query.

Domains:
- HR  → leave, meetings, salary, policies, people matters
- IT  → VPN, laptop, login, tickets, wifi, software issues
- DEV → code, APIs, bugs, deployment, cloud, architecture
- GENERAL → questions directly about the PDF / Annual Report

Return ONLY JSON:
{{ "domain": "HR" | "IT" | "DEV" | "GENERAL" }}

User query:
"{query}"
"""

    response = llm.invoke(prompt).content.strip()

    # Safety cleanup
    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        clean = response[start:end]
        return json.loads(clean)["domain"]
    except:
        return "GENERAL"
