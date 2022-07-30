<?php
$client = new Client();
$headers = [
  'Content-Type' => 'application/json'
];
$body = '{
  "template_name": "general_email",
  "prompt": {
    "email_context": "Part of the same linkedin group",
    "email_subject": "we can improve your traffic by 10x",
    "email_purpose": "Book a demo with us from the input below.",
    "company_description": "We are a company that produces content using natural language generation",
    "from": "Jay",
    "to": "Dom"
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
