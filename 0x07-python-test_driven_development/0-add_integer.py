#!usr/bin/python3
"""
function that adds 2 integers
a and b must be integers or floats
a and b must be first casted to integers if they are float
"""


def add_integer(a, b=98):
    """
        add function adds two integers
        a and b must be integers"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(a, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
