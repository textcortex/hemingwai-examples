<?php
$client = new Client();
$headers = [
  'Content-Type' => 'application/json'
];
$body = '{
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
}';
$request = new Request('POST', 'https://api.textcortex.com/hemingwai/generate_text_v2', $headers, $body);
$res = $client->sendAsync($request)->wait();
echo $res->getBody();
