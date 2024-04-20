#!/usr/bin/python3
""" github api """

if __name__ == "__main__":
    from requests import get
    from sys import argv as av
    user = av[1]
    token = av[2]
    url = "https://api.github.com/users/{}"
    header = {'Authorization': "Bearer {}".format(token)}
    req = get(url.format(user), headers=header)
    print(req.json().get('id'))
