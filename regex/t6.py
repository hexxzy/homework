import re


def checker():
    try:
        login = input("login: ")
        res = re.search(r"[!@#$%^&*()_+]", login)
        if res is not None:
            raise ValueError
        return login
    except ValueError:
        print("Ошибка")


checker()