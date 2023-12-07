#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return None
    new = {}
    for key, v in a_dictionary.items():
        if v != value:
            new[key] = v
    a_dictionary.clear()
    a_dictionary.update(new)
    return new
