#!/usr/bin/python3
"""check if size is integer and greater then 0"""

class Square:
    """This is a simple class"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
