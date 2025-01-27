import ipaddress
import pickle

with open("word-dict.pickle", "rb") as f:
    HEX_WORD_MAP = pickle.load(f)


def hex2word(hx :str):
    if len(hx) > 4: raise Exception("Too long")
    while len(hx) < 4:
        hx = '0'+hx
    hx = hx.upper()
    word = HEX_WORD_MAP[hx]
    return word


def ipv6_2_words(ip :str):
    ip_split = ipaddress.ip_address(ip).compressed.split(':')

    ipwords = []
    for hx in ip_split:
        if hx == '':
            ipwords.append('')
        else:
            ipwords.append(hex2word(hx))


    sentence = ':'.join(ipwords)
    return sentence
    


    






ip_str = input()

print(ipv6_2_words(ip_str))
