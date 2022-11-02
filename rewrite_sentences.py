from textcortex import TextCortex

# Enter your API key Here
YOUR_API_KEY = "YOUR_API_KEY"
hemingwai = TextCortex(api_key=YOUR_API_KEY)


text_to_paraphrase = 'A neuron or nerve cell is an electrically excitable cell that communicates with other' \
                     ' cells via specialized connections called synapses. ' \
                     'The neuron is the main component of nervous tissue in all animals except sponges and placozoa.'

paraphrased_sentence = hemingwai.paraphrase(prompt=text_to_paraphrase, source_language='en', n_gen=4)

for row in paraphrased_sentence:
    print('Paraphrased text: ' + row['text'])