from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import json

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def route_query(query):
    q = query.lower()

    # Rule-based routing (fast & accurate)
    if any(k in q for k in ["leave", "holiday", "salary", "policy", "hr"]):
        return "HR"
    if any(k in q for k in ["vpn", "ticket", "laptop", "software", "login"]):
        return "IT"
    if any(k in q for k in ["code", "api", "bug", "deploy", "cloud"]):
        return "DEV"

    # LLM fallback
    prompt = PromptTemplate.from_template(
        open("prompts/router_prompt.txt").read()
    )

    response = llm.invoke(prompt.format(query=query)).content

    try:
        return json.loads(response).get("domain", "GENERAL")
    except:
        return "GENERAL"
