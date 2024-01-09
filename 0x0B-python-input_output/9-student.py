#!/usr/bin/python3
""" student to json """


class Student:
    """class """
    def __init__(self, first_name, last_name, age):
        """ mr constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ public method fo foo"""
        return (self.__dict__)
