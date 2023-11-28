#!/usr/bin/python3
def fizzbuzz():
    i = 1
    while (i <= 100):
        if (i % 5 == 0 and i % 3 == 0):
            print("FizzBuzz ", end="")
        elif (i % 5 == 0):
            print("Buzz ", end="")
        elif (i % 3 == 0):
            print("Fizz ", end="")
        else:
            print("{:d} ".format(i), end="")
        i += 1

fizzbuzz()
print("")
