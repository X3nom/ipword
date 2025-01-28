#!/usr/bin/python3
import ipaddress
import pickle
import argparse
import importlib.resources
import sys
import re



with importlib.resources.open_binary("ipword_tool.data", "hex-word-dict.pickle") as f:
    WORD_MAP :dict[str, dict[str,str]] = pickle.load(f)

def printErr(msg) -> None: sys.stderr.write(msg+'\n')


def hex2word(hx :str) -> str:
    hx_int = int(hx, 16)

    word = WORD_MAP["hex:word"][hx_int]
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
                hx = hex(WORD_MAP["word:hex"][w])[2:]
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


    address = args.ip_or_word

    if is_ip(address):
        out = ip2word(address)

    else:
        out = word2ip(address)

    print(out)
    

if __name__ == "__main__": main()