import streamlit as st
from agents.router_agent import route_query
from agents.hr_agent import hr_agent
from agents.it_agent import it_agent
from agents.dev_agent import dev_agent
from agents.general_agent import general_agent

st.set_page_config(page_title="HCLTech Agentic RAG Assistant", layout="wide")
st.title("HCLTech Agentic RAG Assistant")

# -----------------------------
# Initialize chat memory
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display chat history
# -----------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").json(msg["content"])

# -----------------------------
# Chat input
# -----------------------------
query = st.chat_input("Ask about HR, IT, DEV or HCLTech Annual Report...")

if query:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").write(query)

    # -----------------------------
    # Build conversational context
    # -----------------------------
    history_text = ""
    for msg in st.session_state.messages[-6:]:
        history_text += f"{msg['role']}: {msg['content']}\n"

    enhanced_query = f"""
Conversation so far:
{history_text}

User's new question:
{query}
"""

    # -----------------------------
    # Routing logic
    # -----------------------------
    # After first document question, stay in GENERAL
    if len(st.session_state.messages) > 2:
        domain = "GENERAL"
    else:
        domain = route_query(enhanced_query)

    # -----------------------------
    # Call correct agent
    # -----------------------------
    if domain == "HR":
        response = hr_agent(enhanced_query)
    elif domain == "IT":
        response = it_agent(enhanced_query)
    elif domain == "DEV":
        response = dev_agent(enhanced_query)
    else:
        response = general_agent(enhanced_query)

    # -----------------------------
    # Save assistant response
    # -----------------------------
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").json(response)
