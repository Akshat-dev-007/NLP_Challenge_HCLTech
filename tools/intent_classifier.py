from langchain_openai import ChatOpenAI
import json

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def classify_intent(domain, query):
    prompt = f"""
You are an intent classifier for domain: {domain}

Decide if the query is:
- action  (needs API/tool)
- knowledge (needs document lookup)

If action, return:
{{"type":"action","function":"<name>","arguments":{{...}}}}

If knowledge, return:
{{"type":"knowledge"}}

Query:
{query}
"""
    try:
        return json.loads(llm.invoke(prompt).content)
    except:
        return {"type": "knowledge"}
