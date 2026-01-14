import streamlit as st
from agents.router_agent import route_query
from agents.hr_agent import hr_agent
from agents.it_agent import it_agent
from agents.dev_agent import dev_agent

st.title("HCL‑Assist (Agentic Enterprise Assistant)")
query = st.text_input("Ask HCL‑Assist")

if query:
    domain = route_query(query)
    st.write("Detected domain:", domain)

    if domain == "HR":
        response = hr_agent(query)
    elif domain == "IT":
        response = it_agent(query)
    elif domain == "DEV":
        response = dev_agent(query)
    else:
        response = {"type": "knowledge", "answer": "General response"}

    st.json(response)
