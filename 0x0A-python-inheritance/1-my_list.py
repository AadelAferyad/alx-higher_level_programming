#!/usr/bin/python3
"""
class MyList that inherits fr list
"""


class MyList(list):
    """ class MyList """
    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
