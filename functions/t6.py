
def factorial():
    a = int(input("Введите число: "))
    sum = 1
    while a > 0:
        sum *= a
        a -= 1
    print("Факториал: ", sum)


factorial()