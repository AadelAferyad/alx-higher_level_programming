#!/usr/bin/python3
""" creating new class """


class Square:
    """ square """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ getter """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ setter """
        if (isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(item, int) and item > 0 for item in value)):
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """ print '#' size times """
        if self.__size == 0:
            print()
        else:
            i = 0
            for j in range(self.__position[1]):
                print()
            while i < self.__size:
                print("{}".format(" " * self.__position[0]), end="")
                print("{}".format("#" * self.__size), end="")
                print()
                i += 1
