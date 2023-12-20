#!/usr/bin/python3
""" class """


class Square:
    """ class def """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """ return square area """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ getter """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ setter """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, obj):
        """ equal """
        return (self.size == obj.size)

    def __lt__(self, obj):
        """ less then """
        return (self.size < obj.size)

    def __le__(self, obj):
        """ less and equal then """
        return (self.size <= obj.size)
