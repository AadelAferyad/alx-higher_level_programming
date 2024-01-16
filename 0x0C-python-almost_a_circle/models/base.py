#!/usr/bin/python3
""" first class everything"""
import json
import os
import csv
import turtle


class Base:
    """Base class !"""
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serializes and deserializes in CSV """
        with open("{}.csv".format(cls.__name__), "w", newline="") as fd:
            if list_objs is None or list_objs == []:
                fd.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnams = ["id", "width", "height", "x", "y"]
                else:
                    fieldnams = ["id", "size", "x", "y"]
                writer = csv.DictWriter(fd, fieldnames=fieldnams)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ serializes and deserializes in CSV """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as fd:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(fd, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw using turtle"""
        ls = ["blue", "red", "green", "purple", "orange", "white", "yellow"]
        ls_2 = ["purple", "yellow", "white", "orange", "green", "red", "blue"]
        if list_rectangles and list_squares:
            screen = turtle.Screen()
            screen.bgcolor("black")
            pen = turtle.Turtle()
            pen.shape("turtle")
            pen.color("white")
            pen.penup()
            pen.forward(-300)
            pen.right(90)
            pen.forward(-250)
            pen.left(90)
            pen.pendown()
            pos = 50
            i = 0
            j = 0
            for obj in list_rectangles:
                dic = obj.to_dictionary()
                pen.color("white", ls[i])
                pen.begin_fill()
                pen.forward(dic["width"])
                pen.right(90)
                pen.forward(dic["height"])
                pen.right(90)
                pen.forward(dic["width"])
                pen.right(90)
                pen.forward(dic["height"])
                pen.end_fill()
                pen.penup()
                pen.right(90)
                pen.forward(dic["width"] + pos)
                pen.pendown()
                i += 1
            pen.penup()
            pen.left(90)
            pen.forward(-300)
            pen.right(90)
            pen.forward(-350)
            pen.pendown()
            for obj in list_squares:
                dic = obj.to_dictionary()
                pen.color("white", ls_2[j])
                pen.begin_fill()
                for x in range(4):
                    pen.forward(dic["size"])
                    pen.right(90)
                pen.end_fill()
                pen.penup()
                pen.forward(dic["size"] + pos)
                pen.pendown()
                j += 1
            screen.exitonclick()
