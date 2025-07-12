import streamlit as st
from components.help_section import render_help_section

st.set_page_config(page_title="Help & Onboarding", layout="centered")

st.title("📖 Help & Onboarding")
render_help_section()
