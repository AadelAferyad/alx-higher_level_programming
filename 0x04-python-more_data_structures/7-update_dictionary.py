#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        return None
    for k, v in a_dictionary.items():
        if key == k:
            a_dictionary[key] = value
            new = dict(a_dictionary)
            return new
    a_dictionary.update({key: value})
    new = dict(a_dictionary)
    return new
