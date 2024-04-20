#!/usr/bin/python3
""" api """
from sys import argv as av
from requests import get, post

if __name__ == "__main__":
    q = ""
    if len(av) > 1:
        q = av[1]
    url = "http://0.0.0.0:5000/search_user"
    req = post(url, data={"q": q})
    try:
        json = req.json()
        if (len(json) == 0):
            print("No result")
        else:
            print(f"[{json.get('id')}] {json.get('name')}")
    except Exception as er:
        print("Not a valid JSON")
