import requests
import json

url = "https://api.textcortex.com/hemingwai/generate_text_v3"

payload = json.dumps({
  "template_name": "email_subject",
  "prompt": {
    "email_keyword": "ai, improve sales, sell more",
    "email_audience": "Sales people who uses hubspot",
    "email_purpose": "Sales",
    "email_context": "We can help you sell more using our AI tool. Would you like to try it?",
    "company_description": "TextCortex AI is a company that produces content using natural language generation technology."
  },
  "temperature": 0.65,
  "token_count": 5,
  "n_gen": 2,
  "source_language": "en",
  "api_key": "YOUR_API_KEY"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
