#!/usr/bin/python3
""" class base of task 8 """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle inherits from BaseGeometry """
    def __init__(self, width, height):
        """ constructor """
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """ area of rectangle """
        return (self.__height * self.__width)

    def __str__(self):
        """ print """
        return (f"[Rectangle] {self.__width}/{self.__height}")
