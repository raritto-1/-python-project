import requests

key = 'Own_api_key'
URL = "https://api.openai.com/v1/chat/completions"

payload = {
    "model": "gpt-4 turbo",
    "messages": [{"role": "user", "content": "What is the first computer in the world?"}],
    "temperature": 1.0,
    "top_p": 1.0,
    "n": 1,
    "stream": False,
    "presence_penalty": 0,
    "frequency_penalty": 0,
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {key}"
}

response = requests.post(URL, headers=headers, json=payload, stream=False)

response_content = response.content

print(response_content)
