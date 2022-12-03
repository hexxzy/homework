import re


def check():
    global MyExeption
    try:
        class MyExeption(Exception):
            pass
        word = input()
        res = re.search(r"[!@#$%^&*]", word)
        if res != None:
            raise MyExeption
        else:
            print(word)
    except MyExeption:
        print("Ошибка.")


check()