#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    length = engthen(tuple_a)
    h = len(tuple_b)
    if (length < 2):
        tuple_a += (0,)
    if h < 2:
        tuple_b += (0,)
    if (length == 0):
        tuple_a += (0, 0,)
    if (h == 0):
        tuple_b += (0, 0,)
    new_tuple = ()
    for i in range(2):
        new_tuple += (tuple_a[i] + tuple_b[i],)
    return (new_tuple)
