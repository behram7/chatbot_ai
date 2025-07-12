 # components/help_section.py
import streamlit as st

def render_help_section():
    with st.expander("📖 **Help & Onboarding Guide**", expanded=False):
        st.markdown("""
## 👋 Welcome!
This app lets you **upload documents**, embed them into **ChromaDB**, and **query them using Groq’s deepseek-r1-distill-llama-70b** through a multi-tenant RAG pipeline.

---

### 📂 **Uploading Documents**
✅ Supported formats: `.pdf` and `.json`  
1. Go to **Upload** in the sidebar.
2. Click **Browse** or drag-and-drop.
3. Follow the **progress bar**.
4. File is embedded into ChromaDB in your private tenant space.

> ⚠️ Each user/tenant has isolated storage and chat history.

---

### 🧠 **Query & Retrieval**
- Enter a **question** in the input box.
- The system:
  - Performs **vector search**.
  - Combines retrieved context (**RAG**) with your prompt.
- Generates a response via Groq’s **deepseek-r1-distill-llama-70b**.

---

### 🪄 **Prompt Engineering Features**
- ✅ Few-shot prompting
- 🧩 Chain-of-thought reasoning
- ⚙️ System-level instructions

Adjust these in the sidebar/settings.

---

### 🗂 **Multi-tenant Pipeline**
Each tenant/user:
- Has a **private ChromaDB collection**
- Keeps uploaded documents private
- Has separate chat sessions

---

### 🖌 **User Interface Tips**
- Built with:
  - `streamlit-shadcn-ui`
  - `streamlit-extras`, `streamlit-lottie`, `streamlit-toggle-switch`
- Use:
  - `st.sidebar` for settings
  - `st.expander` for context/debug
  - `st.columns` for clean layout

---

### 🚀 **Quick Start**
✅ Upload → ✅ Configure prompts → ✅ Ask → ✅ Get answers.

### 💡 **Need help?**
- Built-in tooltips & expander
- User guide PDF (sidebar)
- Contact support

---
        """)
