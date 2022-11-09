#!/usr/bin/python3
"""lists all States from database starting with N"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY 'N'"
                "ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
