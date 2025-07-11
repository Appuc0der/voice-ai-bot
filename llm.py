import requests
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def ask_groq(prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(GROQ_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        print(f"❌ Groq API Error: {response.status_code} - {response.text}")
        return "Sorry, I couldn't get a response from Groq."
