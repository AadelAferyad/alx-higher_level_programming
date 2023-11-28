#!/usr/bin/python3
def uppercase(str):
    lent = len(str)
    b = ''
    for i in range(lent):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            b = chr(ord(str[i]) - 32)
            print("{}".format(b), end="" if i + 1 != lent else "\n")
        else:
            b = chr(ord(str[i]))
            print("{}".format(b), end="" if i + 1 != lent else "\n")
