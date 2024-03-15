#!/usr/bin/python3
"""
This file is for a script that establish a sql connection
and fetch data from a database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__" and len(argv) == 5:
    """
    script that takes in arguments and displays all values
    in the states table of hbtn_0e_0_usa
    where name matches the argument.
    But this time, write one that is safe from MySQL injections!
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        if state[1] == argv[4]:
            print(state)
    db.close()
