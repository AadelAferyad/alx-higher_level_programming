#!/usr/bin/python3

def no_c(my_string):
    length = len(my_string)
    if length == 0:
        return None
    new = ""
    for i in range(length):
        if (ord(my_string[i]) != 67 and ord(my_string[i]) != 99):
            new += my_string[i]
    return (new)
