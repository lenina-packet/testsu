import sqlite3
conn = sqlite3.connect("output/decisions.sqlite")  # любой путь
conn.execute("CREATE TABLE IF NOT EXISTS decisions (id INTEGER PRIMARY KEY, text TEXT)")
conn.commit()
conn.close()
