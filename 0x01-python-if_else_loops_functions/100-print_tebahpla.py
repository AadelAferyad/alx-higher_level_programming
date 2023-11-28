#!/usr/bin/python3

for i in range(26):
    if (i % 2 == 0):
        up = 32
    else:
        up = 0
    print("{}".format(chr((26 - i + 64) + up)), end="")
