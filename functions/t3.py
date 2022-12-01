lst = ["Ильнур", "Ранис", "Ильдар"]


def robot_hello(name):
    if name in lst:
        print(f"Привет, <{name}> !")
    else:
        print(f"Привет, <{name}> ! Рад знакомству!")
        lst.append(name)


robot_hello(input("Введите имя: "))