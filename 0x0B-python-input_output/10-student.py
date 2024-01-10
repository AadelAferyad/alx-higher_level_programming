#!/usr/bin/python3
""" student class dev """


class Student:
    """class """
    def __init__(self, first_name, last_name, age):
        """ mr constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ public method fo foo"""
        if (type(attrs) == list and
                all(type(elements) == str for elements in attrs)):
            var = self.__dict__
            dc = {}
            for key, val in var.items():
                if key in attrs:
                    dc[key] = val
            return (dc)
        return (self.__dict__)
