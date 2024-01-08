#!/usr/bin/python3
""" new class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ new class square """
    def __init__(self, size):
        """ mr constructor """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ area of square """
        return (self.__size * self.__size)
