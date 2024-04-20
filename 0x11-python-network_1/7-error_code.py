#!/usr/bin/python3
""" check status code """
from sys import argv as av
from requests import get
if __name__ == "__main__":
    req = get(av[1])
    if (req >= req.status_code):
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)
