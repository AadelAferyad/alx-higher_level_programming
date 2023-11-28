#!/usr/bin/python3

def remove_char_at(str, n):
    length = len(str)
    s = ''
    for c in range(length):
        if c != n:
            s += str[c]
    return (s)
