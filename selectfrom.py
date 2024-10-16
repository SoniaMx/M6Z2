import sqlite3

conn = sqlite3.connect("cleanfile.db")
cur = conn.cursor()

cur.execute("SELECT * FROM stations LIMIT 5")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()