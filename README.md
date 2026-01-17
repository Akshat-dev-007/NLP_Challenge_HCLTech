# HCLTech Agentic RAG Assistant

An enterprise-grade **Agentic AI + RAG system** designed to enable intelligent, context-aware interaction with enterprise documents and services.  
This assistant can:

-  Chat with PDFs (HCLTech Annual Report)
-  Answer HR, IT, and DEV related queries
-  Trigger actions (e.g., apply leave, raise tickets)
-  Maintain conversational memory
-  Provide citation-grounded responses
-  Output structured JSON actions for automation and demos
-  Support live demonstrations for evaluations/judging

## 🔷 High Level Architecture

```

User (Chat UI)
   ↓
Conversation Memory (Session State)
   ↓
Router Agent (LLM → Domain Selection)
   ↓
Domain Agent (HR / IT / DEV / GENERAL)
   ↓
Intent Detection (Action vs Knowledge)
   ↓
Retriever (Vector DB + MMR)
   ↓
Relevance Gating (Similarity Threshold)
   ↓
LLM Answer Generator
   ↓
Answer + Citations / JSON Action


```

## 📁 Project Structure

```

NLP_HCLTECH/
│
├── app.py
├── agents/
│   ├── router_agent.py
│   ├── hr_agent.py
│   ├── it_agent.py
│   ├── dev_agent.py
│   └── general_agent.py
│
├── tools/
│   ├── retriever.py
│   └── intent_classifier.py   (optional)
│
├── ingestion/
|   ├──chunking.py
|   ├──embedder.py
│   ├── unstructured_loader.py
|
├── index_build.py / rebuild_index.py
│
├──prompts/
|   ├──router_prompt.txt
|
├── vector_store/
│   └── chroma_db/
│
└── README.md

```

## 🛠️ Stepwise Setup: From Virtual Environment to Running the Streamlit App

1️⃣ Create a Virtual Environment
First, go to your project directory:
```
cd NLP_HCLTECH
```
Create a virtual environment:
```
python -m venv venv
```
Activate it:
```
venv\Scripts\activate
```
2️⃣ Install Required Dependencies
```
pip install -r requirements.txt
```
3️⃣ Set Environment Variables
Create a .env file:
```
OPENAI_API_KEY=your_api_key_here
```
4️⃣ Ingest the PDF (Build Vector Store)

Place your PDF inside a folder like:
```
data/
└── Annual-Report-2024-25.pdf
```

Run:
```
rebuild_index.py
```

Expected output:

Semantic blocks: 245
Chunks created: 612
New vector DB built


Now your vector_store/chroma_db/ will be populated.

5️⃣ Verify Vector Store Creation

Check:

vector_store/
└── chroma_db/
    ├── index/
    ├── collections/


If this exists, your retriever is ready.

6️⃣ Launch the Streamlit App

From project root:
```
streamlit run app.py
```

## Few illustrations of our chatbot+RAG based agentic AI applictaion

<img width="1859" height="660" alt="Screenshot 2026-01-16 194256" src="https://github.com/user-attachments/assets/edb0e00e-9042-464a-887e-d41dd2f32320" />
<img width="1768" height="596" alt="Screenshot 2026-01-16 194822" src="https://github.com/user-attachments/assets/86e62fb4-053b-4b43-9043-2f840bc5c752" />
<img width="1792" height="539" alt="image" src="https://github.com/user-attachments/assets/f2f31c67-da7e-44bb-9887-cb918ae39cde" />
<img width="1774" height="522" alt="image" src="https://github.com/user-attachments/assets/f37590c8-22e5-4440-a952-1127db16aba7" />




