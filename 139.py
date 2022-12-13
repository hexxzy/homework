import sqlite3
with sqlite3.connect("PhoneBook.db") as db:
  cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
id integer PRIMARY KEY,
First text NOT NULL,
Surname text NOT NULL,
Phone integer);""")
cursor.execute("""INSERT or IGNORE into Names(id, First, Surname, Phone)
VALUES("2","Karen", "Phillips", "01954 295773")""")
cursor.execute("""INSERT or IGNORE into Names(id, First, Surname, Phone)
VALUES("3", "Darren", "Smith", "01583 749012")""")
cursor.execute("""INSERT or IGNORE into Names(id, First, Surname, Phone)
VALUES("4", "Anne", "Jones", "01323 567322")""")
cursor.execute("""INSERT or IGNORE into Names(id, First, Surname, Phone)
VALUES("5", "Mark", "Smith", "01223 855534")""")
db.commit()
db.close()

