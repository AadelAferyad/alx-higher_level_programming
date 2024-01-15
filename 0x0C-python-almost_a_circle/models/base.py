#!/usr/bin/python3
""" first class everything"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ mr constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json string """
        s = "[]"
        if list_dictionaries is None:
            return (s)
        return (json.dumps(list_dictionaries))
