#!/usr/bin/python3
"""
unction that returns True if the object is an instance of a class
that inherited (directly
or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """ the function """
    return (isinstance(obj, a_class) and not type(obj, a_class))
