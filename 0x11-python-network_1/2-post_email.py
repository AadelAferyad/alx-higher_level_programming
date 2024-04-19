#!/usr/bin/python3
"""sends a POST requests with email """
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv

if len(argv) > 2:
    url = argv[1]
    data = urlencode({'email': argv[2]}).encode('utf-8')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
