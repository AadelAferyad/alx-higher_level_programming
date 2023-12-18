#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while my_list[i] and (i) < x:
            print("{}".format(my_list[i]), end="")
            i += 1
    except Exception as e:
        pass
    finally:
        if i != 0:
            print()
    return (i)



my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(None, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) - 100)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
