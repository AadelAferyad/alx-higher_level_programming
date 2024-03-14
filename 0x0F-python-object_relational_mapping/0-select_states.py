#!/usr/bin/python3
""" this file is for creating a simple sql connection and fetch data """
import MySQLdb
from sys import argv


if __name__ == "__main__" and len(argv) == 4:
    """
    script that lists all states from the database hbtn_0e_0_usa
    this script should't be imported to be able to work!
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    datas = cur.fetchall()
    for data in datas:
        print(data)
    db.close()
