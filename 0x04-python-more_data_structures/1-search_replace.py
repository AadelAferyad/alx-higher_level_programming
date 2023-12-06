#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = []
    for i in range(my_list):
        if search == i:
            new.append(replace)
        else:
            new.append(i)
    return new
