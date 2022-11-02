import requests
import json

url = "https://api.textcortex.com/hemingwai/generate_text_v3"

payload = json.dumps({
  "template_name": "instagram_caption",
  "prompt": {
    "product": "Blue shaded sunglasses with UV protection",
    "target_audience": "University students"
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
