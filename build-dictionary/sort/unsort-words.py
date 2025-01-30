import hashlib


def stable_hash(s: str) -> int:
    return int.from_bytes(hashlib.blake2s(s.encode(), digest_size=8).digest(), "little")


with open("65536-words-alpha-sorted.csv", "r") as f:
    lines = [line.strip().split(',') for line in f.readlines()]
    # use set to unsort the alphabetical order (use python hash for sort)

words = [line[1] for line in lines]

words.sort(key=lambda x: stable_hash(x))


with open("words-hash-sorted.csv", 'w') as f:
    for i in range(len(lines)):
        hx = lines[i][0]
        word = words[i]
        f.write(f"{hx},{word}\n")