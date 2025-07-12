 # components/upload_section.py
import streamlit as st
import time

def render_upload_section():
    st.subheader("📤 Upload Documents")
    st.write("Supported formats: `.pdf` and `.json` only.")

    uploaded_file = st.file_uploader(
        "Choose a file",
        type=['pdf', 'json'],
        help="Only .pdf and .json are supported."
    )

    if uploaded_file is not None:
        file_details = {
            "filename": uploaded_file.name,
            "filetype": uploaded_file.type,
            "filesize": uploaded_file.size
        }
        st.info(f"File: {file_details['filename']} ({round(file_details['filesize']/1024, 2)} KB)")

        # Simulate progress bar (replace this with your embedding logic)
        progress = st.progress(0, text="Embedding document into ChromaDB...")
        for percent in range(100):
            time.sleep(0.01)
            progress.progress(percent + 1, text=f"Progress: {percent+1}%")

        st.success("✅ Document uploaded and embedded successfully!")
