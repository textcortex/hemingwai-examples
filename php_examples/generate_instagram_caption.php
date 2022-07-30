<?php
$client = new Client();
$headers = [
  'Content-Type' => 'application/json'
];
$body = '{
  "template_name": "instagram_caption",
  "prompt": {
    "product": "Blue shaded sunglasses with UV protection",
    "target_audience": "University students"
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
