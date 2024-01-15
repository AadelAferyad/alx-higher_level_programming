#!/usr/bin/python3
""" first class everything"""
import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """ class method"""
        file = cls.__name__ + ".json"
        with open(file, "w", encoding="utf-8") as fd:
            if list_objs is None:
                fd.write("[]")
            else:
                listed = [i.to_dictionary() for i in list_objs]
                fd.write(Base.to_json_string(listed))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON
        string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance
        with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)
            elif cls.__name__ == "Square":
                obj = cls(1)
            obj.update(**dictionary)
            return (obj)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file = cls.__name__ + ".json"
        if not os.path.exists(file):
            return []
        with open(file, "r", encoding="utf-8") as fd:
            ls = cls.from_json_string(fd.read())
        listed = [cls.create(**i) for i in ls]
        return (listed)
