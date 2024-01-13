#!/usr/bin/python3
""" test for base class """
import unittest 
from models.base import Base


class TestClass(unittest.TestCase):
    """ this is a test class """
    def test_norm(self):
        """ normal test for my class"""
        obj = Base(19)
        r = obj.id
        obj_1 = Base()
        r_1 = obj_1.id
        self.assertEqual(r, 19)
        self.assertEqual(r_1, 1)


if __name__ == '__main__':
    unittest.main()