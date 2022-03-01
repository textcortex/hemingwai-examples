import requests

HEMINGWAI_API_KEY = 'SIGNUP_AT_TEXTCORTEX_TO_GET_YOUR_KEY'
HEMINGWAI_GATEWAY = 'https://api.textcortex.com/hemingwai/generate_text'


def generate_instagram_caption(product, audience, character_length, creativity,
                               source_language, n_gen):
    """
    :param product: What is the product that you are promoting
    :param audience: Who is your target audience or target segment?
    :param character_length: How long the generated instagram caption should be?
    :param creativity: Values close to 1 is the highest creativity, 0 is the lowest.
    :param source_language: What is the language of the input you are giving? 'en' for English
    :param n_gen: Number of alternative text to be generted.
    :return:
    """
    try:
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {
            "prompt": product,
            "category": 'Instagram Caption',
            "parameters": audience,
            "character_count": character_length,
            "source_language": source_language,
            # Sets creativity, number between 0 and 1. Default is 0.65
            "creativity": creativity,
            "api_key": HEMINGWAI_API_KEY,
            "n_gen": n_gen
        }
        req = requests.post(HEMINGWAI_GATEWAY, json=data, headers=headers)
        if req.status_code == 403:
            print('API Key is wrong')
            return
        if req.status_code == 402:
            print('Reached API Limits, increase limits by contacting us at dev@textcortex.com or upgrade your account')
            return
        return req.json()['ai_results']
    except Exception as e:
        print(e)
        print('An error occured while making the request')


response = generate_instagram_caption(product='q10 energy face cream',
                                      audience='Middle Aged People',
                                      character_length=500, creativity=0.7, source_language='en', n_gen=3)
i = 1
for row in response:
    print("Generated Text " + str(i) + ": " + row['generated_text'])
    i += 1
