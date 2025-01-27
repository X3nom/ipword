#!/usr/bin/python3
import ipaddress
import pickle
import argparse
import importlib.resources
import sys



with importlib.resources.open_binary("ipword_tool.data", "hex-word-dict.pickle") as f:
    WORD_MAP :dict[str, dict[str,str]] = pickle.load(f)

def printErr(msg) -> None: sys.stderr.write(msg+'\n')


def hex2word(hx :str) -> str:
    if len(hx) > 4: raise Exception("Too long")
    while len(hx) < 4:
        hx = '0'+hx
    hx = hx.lower()
    word = WORD_MAP["hex:word"][hx]
    return word


def ipv6_2_words(ip :str) -> str:
    ip_split = ipaddress.ip_address(ip).compressed.split(':')

    ipwords = []
    for hx in ip_split:
        if hx == '':
            ipwords.append('')
        else:
            ipwords.append(hex2word(hx))
    sentence = ':'.join(ipwords)
    return sentence
    

def ip2word(ip :str) -> str:
    word = ipv6_2_words(ip)
    return word

def word2ip(word :str) -> str:
    words_split = word.split(':')

    ip_parts = []
    for w in words_split:
        if w == '':
            ip_parts.append('')
        else:
            try:
                hx = WORD_MAP["word:hex"][w]
            except KeyError:
                printErr(f"Error: '{w}' is not a valid word nor a part of a valid ip address")
                exit(1)

            ip_parts.append(hx)
            
    fullip = ':'.join(ip_parts)
    try:
        ip = ipaddress.ip_address(fullip).compressed
    except ValueError:
        printErr(f"Error: does not appear to be a valid ip address.\nDecoded address: '{fullip}'")
        exit(1)

    return ip


def is_ip(ip :str) -> bool:
    try:
        ipaddress.ip_address(ip)
        return True
    except: return False



def main():
    parser = argparse.ArgumentParser(prog="ipword", description="Converts ipv6 addresses to more human friendly word representation and back.", epilog="github.com/X3nom/ipword")
    parser.add_argument(
        "ip_or_word",
        metavar="IP/WORD",
        help="Ipv6 address or ipword string (correct setting will be automatically recognized)"
    )

    args = parser.parse_args()
    
    if is_ip(args.ip_or_word):
        word = ip2word(args.ip_or_word)
        print(word)

    else:
        ip = word2ip(args.ip_or_word)
        print(ip)


if __name__ == "__main__": main()