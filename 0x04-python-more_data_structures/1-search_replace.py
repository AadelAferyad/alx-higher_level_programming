#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    if search > len(my_list):
        return my_list
    newlist = [replace if i == search else i for i in my_list]
    return new
