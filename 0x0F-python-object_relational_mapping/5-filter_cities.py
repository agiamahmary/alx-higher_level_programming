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
    sql_state = """SELECT CS.name
                FROM cities AS CS
                INNER JOIN states AS SS
                ON SS.id = CS.state_id
                WHERE SS.NAME = %s
                ORDER BY CS.id"""

    cur.execute(sql_state, (args[4],))

    res = cur.fetchall()

    ans = []

    for row in res:
        for col in row:
            ans.append(col)

    print(", ".join(ans))

    cur.close()
    db.close()
