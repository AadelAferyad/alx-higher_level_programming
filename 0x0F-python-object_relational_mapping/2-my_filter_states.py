#!/usr/bin/python3
"""
This file is for a script that establish a sql connection
and fetch data from a database
"""
from sys import argv
import MySQLdb

if __name__ == "__main__" and len(argv) == 5:
    """
    script that takes in an argument and displays
    all values in the states table of hbtn_0e_0_usa
    where name matches the argument.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], database=argv[3])
    cur = db.cursor()
    q = "SELECT * FROM states WHERE name ='{}'ORDER BY id ASC".format(argv[4])
    cur.execute(q)
    states = cur.fetchall()
    for state in states:
        print(state)
    db.close()
