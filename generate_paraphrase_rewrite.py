import requests
import json

url = "https://api.textcortex.com/hemingwai/generate_text_v3"

payload = json.dumps({
  "template_name": "paraphrase",
  "prompt": {
    "original_sentence": "He also teaches architectural and urban design studios in several universities as an adjunct professor."
  },
  "temperature": 1,
  "token_count": 400,
  "n_gen": 2,
  "source_language": "en",
  "api_key": "YOUR_API_KEY"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
