import pickle


with open("65536-words.csv", "r") as f:
    content = f.readlines()


hex_word = {}
word_hex = {}

for line in content:
    hx, word = line.split(',')
    hx, word = hx.strip().lower(), word.strip().lower()
    
    hex_word.update({hx : word})
    word_hex.update({word : hx})


PICKLE_PROTOCOL = pickle.HIGHEST_PROTOCOL

with open("hex-word-dict.pickle", "wb") as f:
    pickle.dump({
        "hex:word":hex_word,
        "word:hex":word_hex
        }, f, protocol=PICKLE_PROTOCOL)