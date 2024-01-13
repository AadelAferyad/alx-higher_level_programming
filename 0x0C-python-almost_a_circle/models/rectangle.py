#!/usr/bin/python3
""" rect class """
from base import Base


class Rectangle(Base):
    """ rect class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ mr constructor """
        if not isinstance(width, int) and not isinstance(width, float):
            raise TypeError()
        if not isinstance(height, int) and not isinstance(height, float):
            raise TypeError()
        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError()
        if not isinstance(y, int) and not isinstance(y, float):
            raise TypeError()
        if (width <= 0):
            raise ValueError()
        if (height <= 0):
            raise ValueError()
        if (x < 0):
            raise ValueError()
        if (y < 0):
            raise ValueError()
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter for width """
        return (self.__width)

    @width.setter
    def width(self, val):
        """ setter for width """
        if (not isinstance(val, int) and not isinstance(val, float)):
            raise TypeError()
        if (val <= 0):
            raise ValueError()
        self.__width = int(val)

    @property
    def height(self):
        """ this is getter for height"""
        return (self.__height)

    @height.setter
    def height(self, val):
        """ this is setter for height"""
        if (not isinstance(val, int) and not isinstance(val, float)):
            raise TypeError()
        if (val <= 0):
            raise ValueError()
        self.__height = int(val)

    @property
    def x(self):
        """ this getter for x"""
        return (self.__x)

    @x.setter
    def x(self, val):
        """ this is setter for x"""
        if (not isinstance(val, int) and not isinstance(val, float)):
            raise TypeError()
        if (val < 0):
            raise ValueError()
        self.__x = int(val)

    @property
    def y(self):
        """ this is getter for y"""
        return (self.__y)

    @y.setter
    def y(self, val):
        """ this is setter for y"""
        if (not isinstance(val, int) and not isinstance(val, float)):
            raise TypeError()
        if (val < 0):
            raise ValueError()
        self.__y = int(val)
