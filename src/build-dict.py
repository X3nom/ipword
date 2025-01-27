import pickle


with open("65536-words.csv", "r") as f:
    content = f.readlines()


word_dict = {}

for line in content:
    hx, word = line.split(',')
    word_dict.update({hx.strip() : word.strip().lower()})


with open("word-dict.pickle", "wb") as f:
    pickle.dump(word_dict, f)