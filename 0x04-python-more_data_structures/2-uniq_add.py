#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list is None:
        return None
    new = []
    uniq = 0

    for i in my_list:
        not_uniq = False
        for j in new:
            if (i == j):
                not_uniq = True
                break
        if (not not_uniq):
            uniq += i
        new.append(i)
    return uniq
