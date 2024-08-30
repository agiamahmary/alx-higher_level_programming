#!/usr/bin/python3
"""A script that lists all states with a name starting with

    N (upper N) from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    args = sys.argv
    db = MySQLdb.connect(
            host="localhost",
            user=args[1],
            passwd=args[2],
            db=args[3],
            port=3306
        )
    cur = db.cursor()
    sql_state = """
                SELECT id, name
                FROM states
                WHERE name LIKE %s
                ORDER BY id
                """
    cur.execute(sql_state, (args[4],))

    res = cur.fetchall()

    for row in res:
        print(row)

    cur.close()
    db.close()
