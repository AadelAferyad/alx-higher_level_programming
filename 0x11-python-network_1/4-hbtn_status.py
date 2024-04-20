#!/usr/bin/python3
""" using requests modul"""
from requests import get

r = get("https://alx-intranet.hbtn.io/status")
print(f"Body response:\n\t- type: {type(r.text)}\n\t- content: {r.text}")
