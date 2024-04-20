#!/usr/bin/python3
""" send a post request using requests module """
from sys import argv as av
from requests import get, post

url = av[1]
data = {'email': av[2]}
p = post(url, data=data)
req = get(url)
print(p.text)
print(req.text)
