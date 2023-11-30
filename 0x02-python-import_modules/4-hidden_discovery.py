#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4 as hidd
    for name in dir(hidd):
        if not name.startswith('__'):
            print("{}".format(name))
