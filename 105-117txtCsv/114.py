
import csv
start = int(input("Введите начальный год: "))
end = int(input("Введите конечный год: "))
file = list(csv.reader(open("Books.csv", "r")))
tmp = []
for row in file:
 tmp.append(row)
x = 0
for row in tmp:
    if int(tmp[x][2]) >= start and int(tmp[x][2]) <=end:
        print(tmp[x])
    x = x + 1
