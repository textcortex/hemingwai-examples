import requests
import json

url = "https://api.textcortex.com/hemingwai/generate_text_v3"

payload = json.dumps({
  "template_name": "blog_body",
  "prompt": {
    "blog_title": "Why Content is important for your SEO?",
    "blog_keywords": "ai, content generation tools, Search engine optimisation"
  },
  "temperature": 0.65,
  "token_count": 100,
  "n_gen": 2,
  "source_language": "en",
  "api_key": "YOUR_API_KEY"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
