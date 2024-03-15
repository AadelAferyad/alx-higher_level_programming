#!/usr/bin/python3
"""
This file is for a script that establish a sql connection
and fetch data from a database
"""
import MySQLdb
import re
from sys import argv


if __name__ == "__main__" and len(argv) == 4:
    """
    script that lists all states with a name starting
    with N (upper N) from the database hbtn_0e_0_usa.
    this script won't work if it's imported and if not enough
    arrguments
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE \"N%\"")
    states = cur.fetchall()
    for state in states:
        if state[1].startswith('N'):
            print(state)
    db.close()
