import csv
with open("Books.csv", "a") as f:
    title = input("Введите название книги: ")
    author = input("Введите автора: ")
    year = input("Введите год выпуска: ")
    new_book = title + ", " + author + ", " + year + "\n"
    f.write(str(new_book))

    with open("Books.csv", "r") as f:
        for x in f:
            print(x)
            

