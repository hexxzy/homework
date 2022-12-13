import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()
def date():
    year = input("Введите год издания: ")
    cursor.execute("SELECT * FROM Books WHERE datepublished >? ORDER BY datepublished", [year])
    for x in cursor.fetchall():
        print(x)
date()
db.close()
