#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    nayt_max = -1
    m = None
    for key, value in a_dictionary.items():
        if value > nayt_max:
            nayt_max = value
            m = key
    return (m)
