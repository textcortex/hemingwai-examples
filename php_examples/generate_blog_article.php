<?php
$client = new Client();
$headers = [
  'Content-Type' => 'application/json'
];
$body = '{
  "template_name": "blog_body",
  "prompt": {
    "blog_title": "Why Content is important for your SEO?",
    "blog_keywords": "ai, content generation tools, Search engine optimisation"
  },
  "temperature": 0.65,
  "token_count": 100,
  "n_gen": 2,
  "source_language": "en",
  "api_key": "YOUR_API_KEY"
}';
$request = new Request('POST', 'https://api.textcortex.com/hemingwai/generate_text_v3', $headers, $body);
$res = $client->sendAsync($request)->wait();
echo $res->getBody();
