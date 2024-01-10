#!/usr/bin/python3
"""Defines a text file"""


def append_after(filename="", search_string="", new_string=""):
    """insert text"""
    st = ""
    with open(filename) as fd:
        for l in fd:
            st += l
            if search_string in l:
                st += new_string
    with open(filename, "w") as write:
        write.write(st)
