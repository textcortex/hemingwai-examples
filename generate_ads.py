import requests
import json

url = "https://api.textcortex.com/hemingwai/generate_text_v3"

payload = json.dumps({
  "template_name": "ads_copy",
  "prompt": {
    "product_name": "Vegan face cream",
    "target_audience": "Mid aged women",
    "product_category": "Beauty",
    "product_description": "Vegan face cream is an amazing product that helps your skin to replenish its young look while making it shine.",
    "ad_keywords": "vegan, face cream, sustainable"
  },
  "temperature": 0.65,
  "token_count": 200,
  "n_gen": 5,
  "source_language": "en",
  "api_key": "YOUR_API_KEY"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
