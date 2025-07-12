# components/prompt_toggles.py
import streamlit as st

def render_prompt_toggles():
    st.subheader("🪄 Prompt Engineering Options")

    few_shot = st.toggle("Enable Few-Shot Prompting", value=True)
    cot = st.toggle("Enable Chain-of-Thought Reasoning", value=False)
    system_instruction = st.text_area(
        "✏️ System Instructions",
        placeholder="E.g., 'Respond formally and cite sources when possible.'"
    )

    return {
        "few_shot": few_shot,
        "cot": cot,
        "system_instruction": system_instruction
    }
 