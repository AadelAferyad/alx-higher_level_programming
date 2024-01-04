#!/usr/bin/python3
""" this file create a rectangle class """


class Rectangle:
    """ Rectangles properties """
    def __init__(self, width=0, height=0):
        """ initilaze private width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter for width, value must be integer and greater then 0"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ method that return rectangle area """
        if (self.__width and self.__height):
            return (self.__width * self.__height)
        else:
            return (self.width * self.height)

    def perimeter(self):
        """ method that return rectangle perimeter"""
        if (self.__width and self.__height):
            if (self.__width == 0 or self.__height == 0):
                return (0)
            else:
                return 2 * (self.__width + self.__height)
        else:
            if (self.width == 0 or self.height == 0):
                return (0)
            else:
                return 2 * (self.width + self.height)

    def __str__(self):
        """ print """
        string = ""
        if (self.__width and self.__height):
            if (self.__width == 0 or self.__height == 0):
                return (string)
            for i in range(self.__height):
                for j in range(self.__width):
                    string += "#"
                if (i + 1 != self.__height):
                    string += "\n"
        else:
            if (self.width == 0 or self.height == 0):
                return (string)
            for i in range(self.height):
                for j in range(self.width):
                    string += "#"
                if (i + 1 != self.height):
                    string += "\n"
        return (string)

    def __repr__(self):
        """ print rectangle """
        string = "Rectangle("
        if (self.__width and self.__height):
            if (self.__width == 0 or self.__height == 0):
                return ("")
            else:
                string += str(self.__width)
                string += ", "
                string += str(self.__height)
                string += ")"
        else:
            if (self.width == 0 or self.height == 0):
                return ("")
            else:
                string += str(self.width)
                string += ", "
                string += str(self.height)
                string += ")"
        return (string)

    def __del__(self):
        """ deconstructor """
        print("Bye rectangle...")
