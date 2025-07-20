# utils/groq_client.py
from groq import Groq
import os
from dotenv import load_dotenv



load_dotenv()

# Load from env (set GROQ_API_KEY in your environment or deployment secrets)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set. Please set it before running the app.")
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
