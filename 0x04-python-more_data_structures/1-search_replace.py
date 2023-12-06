#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    if search > len(my_list):
        return my_list
    new = []
    for i in range(len(my_list)):
        if search - 1 == i:
            new.append(replace)
        else:
            new.append(my_list[i])
    return new
