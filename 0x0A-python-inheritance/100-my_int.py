#!/usr/bin/python3
""" my class """


class MyInt(int):
    """ class """
    def __eq__(self, other):
        """ == """
        return super().__ne__(other)

    def __ne__(self, other):
        """ != """
        return super().__eq__(other)
