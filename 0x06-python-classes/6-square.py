#!/usr/bin/python3
"""class square"""


class Square:
    """ square """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """ getter """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter """
        if (isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(item, int) and item > 0 for item in value)):
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        """Prints '#' """
        if self.__size == 0:
            print()
        else:
            for new_line in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for dyaz in range(self.__size):
                    print("#", end="")
                print("")
