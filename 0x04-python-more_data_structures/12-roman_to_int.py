#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = roman_string
    val = 0
    for i in range(len(s)):
        if i + 1 < len(s) and r[s[i]] < r[s[i + 1]]:
            val -= r[s[i]]
        else:
            val += r[s[i]]
    return val
