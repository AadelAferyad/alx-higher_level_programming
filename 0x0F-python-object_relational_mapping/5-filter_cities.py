#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

from sys import argv as av
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=av[1],
        password=av[2],
        database=av[3]
    )
    cur = db.cursor()
    query = "SELECT cities.name, states.name FROM cities\
    JOIN states ON states.id = cities.state_id\
    ORDER BY cities.state_id ASC"
    cur.execute(query)
    cities = cur.fetchall()
    j = 0
    for citie in cities:
        if citie[1] == av[4]:
            if j:
                print(end=", ")
            j += 1
            print(citie[0], end="")
    if (not j):
        print()
    db.close()
