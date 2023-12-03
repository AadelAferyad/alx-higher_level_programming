#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if length == 0:
        return None
    if (idx < 0 or idx >= length):
        return (my_list)
    my_list[idx] = element
    return (my_list)
