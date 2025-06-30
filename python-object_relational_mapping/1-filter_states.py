#!/usr/bin/python3
"""This script connects to a MySQL database and retrieves
all states from the 'states' table whose names start with 'N'."""

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # fetch and print all rows
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()