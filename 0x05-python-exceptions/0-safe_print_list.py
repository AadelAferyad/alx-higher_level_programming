#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while my_list[i] and (i) != x:
            print("{}".format(my_list[i]), end="")
            i += 1
        print()
    except booo:
        print()
        return (i)
    return (i)
