import sqlite3
conn = sqlite3.connect("ejdict.sqlite3")
c = conn.cursor()

sql = 'SELECT * FROM sqlite_master'
rows = c.execute(sql)
for n in rows:
    print(n[4])