import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Authors")
    for x in cursor.fetchall():
        print(x)
def placeOfbirthSelection():
    placeOfbirthSelect = input("Поиск по месту рождения: ")
    cursor.execute("""SELECT Books.Title, Books.datepublished, Books.Author
     FROM Books, Authors WHERE Authors.Name = Books.Author AND Authors.placeofbirth=?""", [placeOfbirthSelect])
    for x in cursor.fetchall():
        print(x)
placeOfbirthSelection()
db.close()
