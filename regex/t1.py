def validator():
    try:
        a = int(input("Введите число: "))
        b = a ** 2
        return b
    except ValueError:
        b = "Ошибка."

    finally:
        print(b)


validator()