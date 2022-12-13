import sqlite3
def viewphonebook():
  cursor.execute("SELECT * FROM Names")
  for x in cursor.fetchall():
    print(x)
def addtophonebook():
  new_id = input("Введите ID: ")
  new_name = input("Введите имя: ")
  new_surname = input("Введите фамилию: ")
  new_phone = input("Введите номер телефона: ")
  cursor.execute("""INSERT into Names(id, first, surname, phone)
   VALUES(?, ?, ?, ?)""", (new_id, new_name, new_surname, new_phone))
  db.commit()
def searchforsurname():
  surname_selection = input("Поиск по фамилии: ")
  cursor.execute("""SELECT * FROM Names WHERE surname = ?""", [surname_selection])
  for x in cursor.fetchall():
    print(x)
    db.commit()
def deleteperson():
  delete_id = input("Введите ID для удаления: ")
  cursor.execute("DELETE From Names WHERE id = ?", [delete_id])
  db.commit()

with sqlite3.connect("PhoneBook.db") as db:
  cursor = db.cursor()
menu = input(
  "1) View phone book\n2) Add to phone book\n3) Search for surname\n4) Delete person from phone book\n5)Quit")

if menu == "1":
  viewphonebook()
elif menu == "2":
  addtophonebook()
elif menu == "3":
  searchforsurname()
elif menu == "4":
  deleteperson()
elif menu == "5":
  exit()
else:
    print("Выбрано неверное значение")
db.close()




