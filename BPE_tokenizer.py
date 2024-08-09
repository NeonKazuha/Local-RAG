from transformers import AutoTokenizer
from collections import defaultdict

tokenizer = AutoTokenizer.from_pretrained('gpt2')

word_freq = defaultdict(int)

corpus = open('extraction.txt', 'r').read()

for text in corpus:
    words_with_offsets = tokenizer.backend_tokenizer.pre_tokenizer.pre_tokenize_str(text)
    new_words = [word for word, offset in words_with_offsets]
    for word in new_words:
        word_freq[word] += 1

letters = []

for word in word_freq.keys():
    for letter in word:
        if letter not in letters:
            letters.append(letter)
letters.sort()

vocab = ['<!>'] + letters.copy()

splits = {word: [c for c in word] for word in word_freq.keys()}

def compute_pair_freqs(splits):
    pair_freqs = defaultdict(int)
    for word, freq in word_freqs.items():
        split = splits[word]
        if len(split) == 1:
            continue
        for i in range(len(split) - 1):
            pair = (split[i], split[i + 1])
            pair_freqs[pair] += freq
    return pair_freqs

