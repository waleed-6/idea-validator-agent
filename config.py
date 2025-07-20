import os
import openai
import requests
from openai import OpenAI

# Set your keys here or use .env

SERPER_API_KEY = os.getenv()
client = OpenAI(api_key=)

def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[
            {"role": "system", "content": "You're a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content

def search_serper(query):
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"q": query, "gl": "us", "hl": "en"}
    response = requests.post("https://google.serper.dev/search", headers=headers, json=payload)
    return response.json().get("organic", [])[:3]
