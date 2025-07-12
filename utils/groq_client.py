# utils/groq_client.py
from groq import Groq
import os

# Load from env (create .env and add GROQ_API_KEY)
GROQ_API_KEY = "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"
MODEL_NAME = "deepseek-r1-distill-llama-70b"

client = Groq(api_key=GROQ_API_KEY)

def call_groq_llm(prompt: str, system_instruction: str = "") -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content
