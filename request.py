import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "user",
            "content": "Объясни, что такое токен в LLM"
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

print("Status:", response.status_code)

result = response.json()

print(result["choices"][0]["message"]["content"])