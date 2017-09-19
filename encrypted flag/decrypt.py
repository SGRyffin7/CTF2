#!/usr/bin/env python

def xor(s1, s2):
    res = [chr(0)]*5
    for i in range(len(res)):
        q = ord(s1[i])
        d = ord(s2[i])
        k = q ^ d
        res[i] = chr(k)
    res = ''.join(res)
    return res

with open('encrypted.txt') as f:
    data = f.read()

with open('key') as f:
    key = f.read()

enc = xor(data[0:5], key)

with open('flag', 'wb') as f:
    f.write(enc)
