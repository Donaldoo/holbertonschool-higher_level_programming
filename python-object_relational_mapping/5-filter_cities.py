#!/usr/bin/python3
"""lists all cities from database"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities, states\
                WHERE states.id = cities.state_id AND states.name = %s\
                ORDER BY cities.id", (sys.argv[4], ))
    rows = cur.fetchall()
    separator = ""
    for row in rows:
        print(separator, end="")
        print(row[0], end="")
        separator = ", "
    print()
    cur.close()
    db.close()
