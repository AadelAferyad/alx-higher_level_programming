#!/usr/bin/python3
""" handel errors """
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if len(argv) > 1:
    try:
        with urlopen(argv[1]) as fd:
            print(fd.read().decode('utf-8'))
    except HTTPError as er:
        print(f"Error code: {er.code}")
