#!/usr/bin/python3
""" github api """

if __name__ == "__main__":
    from sys import argv as av
    from requests import get
    repo = av[1]
    owner = av[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    req = get(url)
    cm = req.json()
    for i in range(min(10, len(cm))):
        if cm['message'] != "Git Repository is empty.":
            print(f"{cm[i]['sha']}: {cm[i]['commit']['author']['name']}")
