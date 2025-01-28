# Builds a pickle dictionary from 65536-words.csv for faster access
# source of the wordlist is http://www.webplaces.org/passwords/lists/hexadecimal-65536-list.txt

import pickle


with open("build-dictionary/65536-words.csv", "r") as f:
    content = f.readlines()


hex_word = []
word_hex = {}

for line in content:
    hx, word = line.split(',')
    hx_int, word = int(hx.strip(), 16), word.strip().lower()
    
    hex_word.append(word)
    # hex_word.update({hx_int : word})
    word_hex.update({word : hx_int})


PICKLE_PROTOCOL = pickle.HIGHEST_PROTOCOL

with open("ipword_tool/data/hex-word-dict.pickle", "wb") as f:
    pickle.dump({
        "hex:word":hex_word,
        "word:hex":word_hex
        }, f, protocol=PICKLE_PROTOCOL)