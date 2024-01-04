#!/usr/bin/python3
""" this file create a rectangle class initilaze
    width and height and create setters and getters"""


class Rectangle:
    """ Rectangles properties """
    def __init__(self, width=0, height=0):
        """ initilaze private width and height """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for width, value must be integer and greater then 0"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for Height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter for height, value must be integer and greater then 0"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
