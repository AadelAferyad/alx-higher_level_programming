#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) - 1 == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
