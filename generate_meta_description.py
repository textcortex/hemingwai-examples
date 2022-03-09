import requests

HEMINGWAI_API_KEY = 'SIGNUP_AT_TEXTCORTEX_TO_GET_YOUR_KEY'
HEMINGWAI_GATEWAY = 'https://api.textcortex.com/hemingwai/generate_text'


def generate_meta_description(page_title, page_keywords, character_length, creativity,
                              source_language, n_gen):
    """
    :param page_title: What is the title of the page that you want to generate meta descriptions for?
    :param page_keywords: Give some keywords that can help TextCortex to understand what this page is about, don't
    forget to seperate each keyword using commas.
    :param character_length: Defines the length of generated meta descriptions
    :param creativity: A number between 0 and 1. 0 is the lowest creativity, 1 is the highest.
    :param source_language: Use 'en' for English, for other languages use the correct language code
    :param n_gen: Defines how many alternatives will be generated.
    :return:
    """
    try:
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {
            "prompt": page_title,
            "category": 'Meta Description',
            "parameters": page_keywords,
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


response = generate_meta_description(page_title='Urban Fast Intro Video Template',
                                     page_keywords="video templates, stock videos, design elements, openers, "
                                                   "adobe after effects",
                                     character_length=300, creativity=0.5, source_language='en', n_gen=3)
# Response includes rich data with focus keywords in it, let's check out the results
i = 1
for row in response:
    print("Generated Text " + str(i) + ": " + row['generated_text'])
    i += 1
