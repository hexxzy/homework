a = open("Names.txt", "a")
name = input("Введите имя: ")
a.write(f"\n{name}")
a.close()
b = open("Names.txt", "r")
print(b.read())
b.close()


