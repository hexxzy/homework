def login():
    BD = {}
    while True:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        passw = BD.get(login)
        if passw == password:
            print("Вы успешно авторизовались")
        elif not passw:
            BD[login] = password
            print("Регистрация прошла успешно")
        else:
            print("Неверный пароль, доступ запрещен")
            break


login()