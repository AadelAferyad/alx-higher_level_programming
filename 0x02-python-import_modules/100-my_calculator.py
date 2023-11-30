#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    def switcher(val, a, b):
        if val == '+':
            return add(a, b)
        elif val == '-':
            return sub(a, b)
        elif val == '*':
            return mul(a, b)
        elif val == '/':
            return div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    argc = len(sys.argv)
    if (argc - 1) != 3:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        op = sys.argv[2]
        r = switcher(op, a, b)
        print("{} {} {} = {}".format(a, op, b, r))
