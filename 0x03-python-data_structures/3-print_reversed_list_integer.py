#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        length = len(my_list)
        for i in range(length):
            print("{:d}".format(my_list[::-1][i]))
