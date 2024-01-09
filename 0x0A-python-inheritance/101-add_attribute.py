#!/usr/bin/python3
""" 1337 """


def add_attribute(object, attr, value):
    """ add class """
    if hasattr(object, '__dict__'):
        setattr(object, attr, value)
    else:
        raise TypeError("can't add new attribute")
