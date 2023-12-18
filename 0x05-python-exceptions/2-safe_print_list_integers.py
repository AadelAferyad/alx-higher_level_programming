#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (IndexError, TypeError, ValueError):
            i += 1
            continue
        i += 1
    print()
    return (i)
