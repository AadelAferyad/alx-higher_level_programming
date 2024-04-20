#!/usr/bin/python3
"""
20/4/2024 2am blati mix, high hamdolilah
alx almost done , fin ana wtf fin ghadi chkon ana
"""
from requests import get
from sys import argv as av
if len(av) > 1:
    r = get(av[1])
    print(r.headers['X-Request-Id'])
