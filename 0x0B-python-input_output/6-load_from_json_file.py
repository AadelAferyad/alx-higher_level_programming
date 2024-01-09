#!/usr/bin/python3
""" file.json """
import json


def load_from_json_file(filename):
    """function that creates an Object from a 'JSON file'"""
    with open(filename, 'r', encoding="utf-8") as fd:
        return (json.loads(fd.read()))
