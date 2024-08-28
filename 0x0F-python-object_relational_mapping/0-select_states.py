#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


args = sys.argv
db = MySQLdb.connect(
        host="localhost",
        user=args[1],
        passwd=args[2],
        database=args[3],
        port=3306
    )
cur = db.cursor()
cur.execute("SELECT id, name FROM states ORDER BY id")
res = cur.fetchall()

for row in res:
    print(row)

cur.close()
db.close()
