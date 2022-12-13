import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()
    txtRecord = input("Введите имя автора: ")
    cursor.execute("""SELECT * FROM Books WHERE Author=?""", [txtRecord])
    for x in cursor.fetchall():
        with open("authorRecords.txt", "a") as f:
            with open("authorRecords.txt", "a") as f:
             f.write(str(x[0]) + " - " + x[1] + " - " + x[2] + " - " + str(x[3]) + "\n")
db.close()


