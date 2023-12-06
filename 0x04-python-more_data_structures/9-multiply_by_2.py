#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    new = dict(a_dictionary)
    for key, value in new.items():
        new[key] = value * 2
    return new
