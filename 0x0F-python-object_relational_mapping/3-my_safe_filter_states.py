#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    safe = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s"
                "ORDER BY states.id", (safe, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
