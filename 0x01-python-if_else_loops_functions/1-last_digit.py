#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 0
si = ''
betty = "and is less than 6 and not 0"
if number < 0:
    si = '-'
    number *= -1
    sign = -1
else:
    sign = 1
last = number % 10
if (last * sign) == 0:
    print(f"Last digit of {si}{number} is {number % 10} and is {number % 10}")
elif (last * sign) > 5:
    print(f"Last digit of {number} is {number % 10} and is greater than 5")
elif (last * sign) < 6 and (last * sign) != 0:
    print(f"Last digit of {si}{number} is {si}{last} {betty}")
