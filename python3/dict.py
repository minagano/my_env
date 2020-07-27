import sqlite3

conn = sqlite3.connect("ejdict.sqlite3")
c = conn.cursor() #コネクションからカーソルを取得してｃに入れる

sql = 'SELECT * FROM items LIMIT 10'
rows = c.execute(sql)
for n in rows:
    print(n)