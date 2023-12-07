#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None:
        return None
    multi = 0
    al = 0
    for i in my_list:
        al += i[0] * i[1]
        multi += i[1]
    if multi == 0:
        multi = 1
    return al / multi
