#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except (TypeError, ZeroDivisionError, ValueError, IndexError) as boo:
        print("Exception: {}".format(boo), file=sys.stderr)
        return (None)
