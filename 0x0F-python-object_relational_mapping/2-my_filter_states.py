#!/usr/bin/python3
"""A script that takes in an argument and displays all values in the states

    table of hbtn_0e_0_usa where name matches the argument
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
    sql_state = """SELECT id, name
                FROM states
                WHERE BINARY name='{}'
                ORDER BY id""".format(args[4])

    cur.execute(sql_state)

    res = cur.fetchall()

    for row in res:
        print(row)

    cur.close()
    db.close()
