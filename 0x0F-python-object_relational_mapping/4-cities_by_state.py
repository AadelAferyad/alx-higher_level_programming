#!/usr/bin/python3
"""
This file is for a script that establish a sql connection
and fetch data from a database
"""

import MySQLdb as sql
from sys import argv as av

if __name__ == "__main__" and len(av) == 4:
    """
    script that lists all cities from the database hbtn_0e_4_usa
    """
    db = sql.connect(
        host="localhost",
        port=3306,
        user=av[1],
        password=av[2],
        database=av[3]
    )
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name\
    FROM cities JOIN states ON cities.state_id = states.id"
    cur.execute(query)
    cities = cur.fetchall()
    for citie in cities:
        print(citie)
    db.close()
