#!/usr/bin/python3
# -*- coding: utf-8 -*-
# DA+Nils 2018
# Andrei + Z.TANG + Bowen, 2019
# SUTD 50.042 FCS Lab 2
# See Wan Yi Faith (1002851)

"""
Lab2: Breaking Ciphers

Pwntool client for python3

Install: see install.sh

Documentation: https://python3-pwntools.readthedocs.io/en/latest/
"""

from pwn import remote
import string
import re

# pass two bytestrings to this function
def XOR(a, b):
    r = b''
    for x, y in zip(a, b):
        r += (x ^ y).to_bytes(1, 'big')
    return r


def sol1():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("1")  # select challenge 1

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    print(challenge)
    # decrypt the challenge here

    # 1. creating a dictionary with the characters of string.printable for the challenge
    sp_dict_c = {}
    for char in string.printable:
        sp_dict_c[char] = 0
    print(sp_dict_c)

    # 2a. conduct frequency analysis with challenge
    for char in challenge.decode():
        if char in sp_dict_c:
            sp_dict_c[char] += 1
    print(sp_dict_c)
    print('\n')
    # 2b. print sorted frequency analysis
    print("Sorted frequency analysis from challenge:")
    sorted_fa_c = sorted(sp_dict_c.items(), key=lambda kv:kv[1], reverse=True)
    print(sorted_fa_c)
    print('\n')

    # 3. creating a dictionary with the characters of string.printable for the sample
    sp_dict_s = {}
    for char in string.printable:
        sp_dict_s[char] = 0
    # print(sp_dict_s)

    # 4a. conduct frequency analysis with sample story (sample.txt)
    with open('sample.txt', 'r') as fin:
        text = fin.read()
        for char in text:
            if char in sp_dict_s:
                sp_dict_s[char] += 1
        # print(sp_dict_s)
        # print('\n')

        # 4b. print sorted frequency analysis
        print("Sorted frequency analysis from sample:")
        sorted_fa_s = sorted(sp_dict_s.items(), key=lambda kv:kv[1], reverse=True)
        # sorted_fa_s = sorted(sp_dict_s, key=sp_dict_s.get, reverse=True)
        print(sorted_fa_s)
    fin.close()

    #5. create new dictionary with keys from frequency analysis of cipher and values from frequency analysis of sample
    mapping_dict = {}
    for i in range(len(string.printable)):
        mapping_dict[sorted_fa_c[i][0]] = sorted_fa_s[i][0]
    print('\n')
    print('Mapping dictionary:')
    print(mapping_dict)

    #6. Loop through cipher text and use char as key to find corresponding value to append to string / byte array
    decoded = []
    for char in challenge.decode():
        if mapping_dict.get(char) == '"':
            decoded.append("v")
        elif mapping_dict.get(char) == '?':
            decoded.append("q")
        elif mapping_dict.get(char) == "'":
            decoded.append("j")
        elif mapping_dict.get(char) == "j":
            decoded.append("'")
        elif mapping_dict.get(char) == "v":
            decoded.append('"')
        elif mapping_dict.get(char) == "q":
            decoded.append('?')
        else:
            decoded.append(mapping_dict.get(char))
    solution = ''.join(decoded)
    print(solution)

    conn.send(solution)
    message = conn.recvline()
    message = conn.recvline()
    if b'Congratulations' in message:
        print(message)
    conn.close()


def sol2():
    conn = remote(URL, PORT)
    message = conn.recvuntil('-Pad')  # receive TCP stream until end of menu
    conn.sendline("2")  # select challenge 2

    dontcare = conn.recvuntil(':')
    challenge = conn.recvline()
    # some all zero mask.
    # TODO: find the magic mask!
    # mask = int(0).to_bytes(len(message), 'big')
    mask = XOR(b'Student ID 1000000 gets 0 points\n', b'Student ID 1002851 gets 4 points\n')
    message = XOR(challenge, mask)
    conn.send(message)
    message = conn.recvline()
    message = conn.recvline()
    if b'points' in message:
        print(message)
    conn.close()


if __name__ == "__main__":

    # NOTE: UPPERCASE names for constants is a (nice) Python convention
    URL = '34.239.117.115'
    PORT = 1337

    sol1()
    sol2()
