#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            new.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            new.append(0)
        except TypeError:
            print("wrong type")
            new.append(0)
        except IndexError:
            print("out of range")
            new.append(0)
        finally:
            pass
    return new
