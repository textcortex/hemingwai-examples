<?php
$client = new Client();
$headers = [
  'Content-Type' => 'application/json'
];
$body = '{
  "template_name": "paraphrase",
  "prompt": {
    "original_sentence": "It was a great day at cortex HQ."
  },
  "temperature": 1.3,
  "word_count": 20,
  "n_gen": 4,
  "source_language": "en",
  "api_key": "YOUR_API_KEY"
}';
$request = new Request('POST', 'https://api.textcortex.com/hemingwai/generate_text_v2', $headers, $body);
$res = $client->sendAsync($request)->wait();
echo $res->getBody();
