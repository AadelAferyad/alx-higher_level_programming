#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

from sys import argv as av
import MySQLdb

if __name__ == "__main__" and len(av) == 5:

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=av[1],
        password=av[2],
        database=av[3]
    )
    cur = db.cursor()
    query = "SELECT cities.name FROM cities\
    JOIN states ON states.id = cities.state_id\
    WHERE states.name = '{}' \
    ORDER BY cities.state_id ASC".format(av[4])
    cur.execute(query)
    cities = cur.fetchall()
    j = 0
    for citie in cities:
        j += 1
        print(citie[0], end=", " if (j > 0 and j < len(cities)) else "")

    print()
    db.close()
