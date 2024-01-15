#!/usr/bin/python3
""" rect class """
from models.base import Base
# from base import Base


class Rectangle(Base):
    """ rect class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ mr constructor """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        if (height <= 0):
            raise ValueError("height must be > 0")
        if (x < 0):
            raise ValueError("x must be >= 0")
        if (y < 0):
            raise ValueError("y must be >= 0")
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
        if type(val) != int:
            raise TypeError("width must be an integer")
        if (val <= 0):
            raise ValueError("width must be > 0")
        self.__width = int(val)

    @property
    def height(self):
        """ this is getter for height"""
        return (self.__height)

    @height.setter
    def height(self, val):
        """ this is setter for height"""
        if type(val) != int:
            raise TypeError("height must be an integer")
        if (val <= 0):
            raise ValueError("height must be > 0")
        self.__height = int(val)

    @property
    def x(self):
        """ this getter for x"""
        return (self.__x)

    @x.setter
    def x(self, val):
        """ this is setter for x"""
        if type(val) != int:
            raise TypeError("x must be an integer")
        if (val <= 0):
            raise ValueError("x must be >= 0")
        self.__x = int(val)

    @property
    def y(self):
        """ this is getter for y"""
        return (self.__y)

    @y.setter
    def y(self, val):
        """ this is setter for y"""
        if type(val) != int:
            raise TypeError("y must be an integer")
        if (val <= 0):
            raise ValueError("y must be >= 0")
        self.__y = int(val)

    def area(self):
        """ area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """ display method"""
        if (self.__y > 0):
            for y in range(self.__y):
                print("")
        for i in range(self.__height):
            print(end=" " * self.__x if self.x > 0 else "")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ str magic method"""
        return (f"[Rectangle] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """ update using args """
        if len(args) != 0:
            if len(args) >= 1:
                if args[0] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
