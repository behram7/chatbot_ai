# app.py
import streamlit as st
from components.upload_section import render_upload_section
from components.prompt_toggles import render_prompt_toggles
from components.help_section import render_help_section
from components.lottie_onboarding import render_lottie_animation
import logging


from utils.groq_client import call_groq_llm
from utils.chroma_client import get_or_create_collection, embed_and_store_document, query_collection
from utils.file_utils import extract_text_from_pdf, extract_text_from_json, split_text_into_chunks

st.set_page_config(page_title="Groq RAG App", layout="wide")

st.title("📄 Multi-Tenant RAG with Groq + ChromaDB")

tenant_id = st.text_input("🧑 Tenant ID / Username", value="default_tenant")

col1, col2 = st.columns([2, 1])

with col1:
    render_lottie_animation("assets/lottie_onboarding.json", height=200)

    st.subheader("📤 Upload Documents")
    uploaded_file = st.file_uploader("Choose .pdf or .json", type=["pdf", "json"])

    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            text = extract_text_from_pdf(uploaded_file)
        else:
            text = extract_text_from_json(uploaded_file)

        text_chunks = split_text_into_chunks(text)
        st.info(f"Extracted {len(text_chunks)} chunks for embedding.")

        collection = get_or_create_collection(tenant_id)
        embed_and_store_document(collection, text_chunks, metadata={"filename": uploaded_file.name})

        st.success("✅ Document embedded into ChromaDB.")

    prompt_settings = render_prompt_toggles()

    query = st.text_input("💬 Ask a question:")
    if query:
        collection = get_or_create_collection(tenant_id)
        search_results = query_collection(collection, query)

        # Aggregate retrieved chunks
        retrieved_context = "\n".join([doc for docs in search_results["documents"] for doc in docs])

        full_prompt = f"Context: {retrieved_context}\n\nUser question: {query}"

        answer = call_groq_llm(
            prompt=full_prompt,
            system_instruction=prompt_settings['system_instruction']
        )

        st.markdown(f"### 🤖 Answer:\n{answer}")

with col2:
    render_help_section()


logging.basicConfig(level=logging.INFO)
