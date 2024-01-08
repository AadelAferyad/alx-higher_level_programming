#!/usr/bin/python3
"""
class MyList that inherits fr list
"""


class MyList(list):
    """ class MyList """
    def __init__(self):
        """ constructor """
        super().__init__()

    def print_sorted(self):
        """ print sorted list """
        tmp = self.copy()
        tmp.sort()
        print(tmp)
