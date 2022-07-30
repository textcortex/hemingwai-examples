# hemingwai-examples
This repo contains examples regarding TextCortex API namely; Hemingwai.

Textcortex AI uses fine tuned models for application specific needs. Accessing them is as easy as making an API call.

## How To Generate Content:
1. Signup at https://textcortex.com
2. Sign-in and click on account on top right.
3. Go to API Key section and copy your key.
4. Make a POST request to https://api.textcortex.com/hemingwai/generate_text_v2

### Types Of Content That Can Be Generated with TextCortex API:
- Generate Product Descriptions
- Generate Blog Articles
- Generate Meta Descriptions
- Generate Instagram Captions
- Generate PPC Ads
- Generate Email Body
- Generate Email Subject

### Here is an example POST request for generating Product Descriptions:

```
import requests
import json

url = "https://api.textcortex.com/hemingwai/generate_text_v2"

payload = json.dumps({
  "template_name": "product_description",
  "prompt": {
    "product_name": "Blue sports underwear",
    "brand": "Nike",
    "product_category": "Clothing",
    "product_features": "Ultra soft and super well wet absorbing"
  },
  "temperature": 0.65,
  "word_count": 200,
  "n_gen": 2,
  "source_language": "en",
  "api_key": "YOUR_API_KEY"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

The response would be like the following:
```
{
    "status": "success",
    "generated_text": [
        {
            "text": "In addition to the standard color Nike Dri-Fit, the Nike Dri-Fit Blue is available in two other colors as well. The Nike Dri-Fit Blue is made of a special blend of spandex and elastane that is soft, ultra soft, and super well wet absorbing. It is designed for comfort and performance with a soft interior to help keep you cool and dry even after an intense workout.",
            "id": "d7873828-0d1d-4961-a3a4-0f797c9a9218"
        },
        {
            "text": "Nike Men's Men's Blue Sports Running Shorts.",
            "id": "bb1f65b2-a660-4f33-8535-ffd5d86d16ee"
        }
    ],
    "remaining_requests": 86,
    "error": 200
}
```
Rest of the examples together with PHP scripts can be found under root directory. If you have questions, contact us at dev@textcortex.com


