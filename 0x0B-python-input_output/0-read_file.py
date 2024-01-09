#!/usr/bin/python3
""" file containe one function """


def read_file(filename=""):
    """ open a file and read it's content """
    if filename is not None:
        with open(filename, 'r', encoding="utf-8") as a:
            print(a.read())
