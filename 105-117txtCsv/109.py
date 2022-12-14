menu = input("1) Create a new file\n2) Display the file\n3) Add a new item to the file\nMake a selection 1, 2 or 3: ")
if menu == "1":
  lesson = input("Введите название школьного предмета: ")
  sub = open("Subject.txt", "w")
  sub.write(f"\n1{lesson}")
  sub.close()
elif menu == "2":
  sub = open("Subject.txt", "r")
  print(sub.read())
  sub.close()
elif menu == "3":
  lesson = input("Введите название школьного предмета: ")
  sub = open("Subject.txt", "a")
  sub.write(f"\n{lesson}")
  sub.close()
  sub_read = open("Subject.txt", "r")
  print(sub_read.read())
  sub_read.close()
else:
  print("ERROR")

