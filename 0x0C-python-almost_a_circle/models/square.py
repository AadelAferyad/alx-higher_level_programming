#!/usr/bin/python3
""" this file is for square class"""
from models.rectangle import Rectangle
# Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """ this class is for square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ mr constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ magic method for square"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """ getter for size"""
        return (self.width)

    @size.setter
    def size(self, v):
        """ setter for size"""
        self.width = v
        self.height = v

    def update(self, *args, **kwargs):
        """ update square"""
        if len(args) != 0:
            if len(args) >= 1:
                if args[0] is None:
                    super().__init__(self.size, self.size, self.x, self.y)
                else:
                    self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        super().__init__(self.size, self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
