#!/usr/bin/python3

for a in range(90, 64, -1):
    if a % 2 == 0:
        a = a + 32
        print("{:c}".format(a), end="")
    else:
        print("{:c}".format(a), end="")