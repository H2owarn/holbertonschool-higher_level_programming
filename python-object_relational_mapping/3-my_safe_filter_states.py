#!/usr/bin/python3

"""This script connects to a MySQL database and retrieves
all states from the 'states' table
whose names match a given state name
and safe from SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname)

    cur = db.cursor()
    query = (
        "SELECT * "
        "FROM states "
        "WHERE BINARY name = %s "
        "ORDER BY id ASC"
    )

    cur.execute(query, (state_name))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
