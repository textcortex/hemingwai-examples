import requests
import json

url = "https://api.textcortex.com/hemingwai/generate_text_v3"

payload = json.dumps({
  "template_name": "general_email",
  "prompt": {
    "email_context": "Part of the same linkedin group",
    "email_subject": "we can improve your traffic by 10x",
    "email_purpose": "Book a demo with us from the input below.",
    "company_description": "We are a company that produces content using natural language generation",
    "from": "Jay",
    "to": "Dom"
  },
  "temperature": 0.65,
  "token_count": 200,
  "n_gen": 2,
  "source_language": "en",
  "api_key": "YOUR_API_KEY"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
