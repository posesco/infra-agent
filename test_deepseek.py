import os
import requests

api_key = os.getenv("DEEPSEEK_API_KEY")
url = "https://api.deepseek.com/v1/chat/completions"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Hola, ¿puedes ayudarme a diseñar una arquitectura AWS resiliente?"}]
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
