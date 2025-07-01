#!/usr/bin/python3

"""This script connects to a MySQL database and retrieves
all cities from the 'cities' table
that belong to a specific state"""

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
        db=dbname
    )

    cur = db.cursor()
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC "
    )

    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    for row in rows:
        print(", ".join(row[0] for row in rows))

    cur.close()
    db.close()
