#!/usr/bin/python3

"""This script connects to a MySQL database and retrieves all rows from the 'states' table,
ordering them by the 'id' column in ascending order.
It requires three command line arguments: username, password, and database name.
It uses the MySQLdb library to connect to the database and execute the query.
"""

import MySQLdb
import sys

if __name__ == "__main__":


    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect (
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    #  fetch and print all rows
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
    # close the cursor and database connection
