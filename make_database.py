import sqlite3

conn = sqlite3.connect("database.db")
print("DB open!")

sql = "CREATE TABLE pages (url TEXT, html TEXT)"
conn.execute(sql)
print("Table created!")
conn.close()