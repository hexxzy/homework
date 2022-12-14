num = int(input("Сколько записей вы хотите сделать?"))
file = open("Books.csv", "a")
for x in range(0, num):
 title = input("Введите название: ")
 author = input("Введите автора: ")
 year = input("Введите год выпуска: ")
 newrecord = title + ", " + author + ", " + year + "\n"
 file.write(str(newrecord))
file.close()
searchauthor = input("Введите автора для поиска: ")
file = open("Books.csv", "r")
count = 0
for x in file:
     if searchauthor in str(x):
        print(x)
count = count + 1
if count == 0:
 print ("Книги данного автора нет в списке")
file.close()
