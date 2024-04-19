#!/usr/bin/python3
from sys import argv
import urllib.request

if len(argv) > 1:
    with urllib.request.urlopen(argv[1]) as res:
        body = res.getheaders()
        for i in body:
            a, b = i
            if a == "X-Request-Id":
                print(b)
                break
