# hemingwai-examples
This repo contains examples regarding TextCortex API namely; Hemingwai.

Textcortex AI uses fine tuned models for application specific needs. Accessing them is as easy as making an API call.

## How To Generate Content:
1. Signup at https://textcortex.com
2. Sign-in and click on account on top right.
3. Go to API Key section and copy your key.
4. Make a POST request to http://api.textcortex.com/hemingwai/generate_text

### Here is an example POST request for generating Product Descriptions:

```
import requests

HEMINGWAI_API_KEY = 'SIGNUP_AT_TEXTCORTEX_TO_GET_YOUR_KEY'
HEMINGWAI_GATEWAY = 'https://api.textcortex.com/hemingway/generate_text'

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data = {
            "prompt": "Blue Satin Wedding Dress",
            "category": "Product Description",
            "parameters": "Category: ['Clothing', 'Women']",
            "character_count": character_length,
            "source_language": source_language,
            "creativity": creativity, # Sets creativity, number between 0 and 1. Default is 0.65
            "api_key": HEMINGWAI_API_KEY,
            "n_gen": 2 # Sets how many samples to be generated
}
req = requests.post(HEMINGWAI_GATEWAY, json=data, headers=headers)
```

The response would be like the following:
```
{
    "status": "success",
    "ai_results": [
        {
            "generated_text": " This is a gorgeous and unique dress perfect for your coming event. The dress has a lovely V neckline and a flattering waistline that will fit in all sizes. The fabric is soft and comfortable.The material is chiffon which is the best choice for you and your friends. This dress is for every woman who wants to look beautiful while feeling effortless.\n",
            "rank": 0.9561,
            "text_length": 433,
            "word_frequency": [
                {
                    "word": "soft",
                    "frequency": 3
                },
                {
                    "word": "material",
                    "frequency": 3
                },
                {
                    "word": "dress",
                    "frequency": 3
                },
                {
                    "word": "comfortable",
                    "frequency": 3
                }
            ],
            "word_count": 76
        }, ....
```

Rest of the example can be found under root directory. If you have questions, contact us at dev@textcortex.com


