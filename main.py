

import sqlite3
connection=sqlite3.connect("videos.db")
cursor=connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS videos(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT,
                Views INTEGER ,
                Category TEXT
                )""")
title=input("Enter Video title:")
views=int(input("Enter the number of Views:"))
category=input("Enter the Video category:")
cursor.execute("INSERT INTO videos(Title,Views,Category) VALUES (?,?,?)"
               ,(title,views,category))
cursor.execute("SELECT * FROM videos")
rows=cursor.fetchall()
for row in rows:
    print("ID:", row[0])
    print("Title:", row[1])
    print("Views:", row[2])
    print("Category:", row[3])
    print("-------------------")
connection.commit()
connection.close()
