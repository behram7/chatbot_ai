# Chatbot AI

A Streamlit-based web application for uploading `.pdf` and `.json` documents, embedding them into ChromaDB, and interacting with them using AI.

## Features

- Integrates with *Groq’s LLM API* using the model deepseek-r1-distill-llama-70b
- Uses *ChromaDB* as a vector store to implement a *multi-tenant RAG pipeline*
- Offers advanced *prompt engineering techniques* including:
  - Few-shot prompting
  - Chain-of-thought reasoning
  - System-level prompt configuration
- Implements a *document upload interface* with:
  - File-type restriction (.pdf and .json only)
  - Upload progress bar
  - User guidance/help section on supported formats and usage
- Includes *persistent chat sessions* and isolated history per tenant/user
- Uses a *modern, sleek UI* built with:
  - streamlit-shadcn-ui for Tailwind-style aesthetics
  - streamlit-extras, streamlit-lottie, streamlit-toggle-switch, and others
- Follows a *clean folder structure* with all files organized by responsibility

---

## 🎯 Functional Goals

### ✅ Core Features
- [x] Document Upload with Progress Bar
- [x] Embedding of uploaded content into ChromaDB (per tenant)
- [x] Vector search with metadata filters
- [x] Query input and Groq-powered LLM response (with context via RAG)
- [x] Multi-tenant user isolation (separate collections + chat sessions)
- [x] Intuitive prompt engineering (CoT + system instructions)
- [x] Streamlit layout with st.columns, st.sidebar, st.expander, etc.
- [x] Onboarding/help section explaining how to use the app

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/chatbot_ai.git
   cd chatbot_ai
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## Deployment

You can deploy this app for free using [Streamlit Community Cloud](https://streamlit.io/cloud):
1. Push your code to a public GitHub repository.
2. Sign in to Streamlit Cloud and create a new app from your repo.
3. Set any required environment variables in the app settings.
4. Share your app's public URL!

## Project Structure
```
chatbot_ai/
  app.py
  components/
    help_section.py
    lottie_onboarding.py
    prompt_toggles.py
    upload_section.py
  pages/
    Help.py
  utils/
    chroma_client.py
    file_utils.py
    groq_client.py
    prompts.py
  assets/
    lottie_onboarding.json
  requirements.txt
```


