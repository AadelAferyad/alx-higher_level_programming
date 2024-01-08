#!/usr/bin/python3
""" function that returns the list
of available attributes and methods of an object
"""


def lookup(obj):
    """ the function"""
    if obj is not None:
        return (dir(obj))
