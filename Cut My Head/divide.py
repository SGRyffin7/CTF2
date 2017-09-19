#!/usr/bin/env python

with open('encrypted.out') as f:
    data = f.read()

for i in range(0, len(data), 8):
    if i+8 <= len(data):
        print data[i:i+8]
	print "\n"
    else:
        print data[i:]
	print "\n"
