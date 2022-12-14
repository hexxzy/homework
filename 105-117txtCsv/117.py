import csv
from random import randint


name = input("введите имя: ")
question = [
    "как настроение? ",
    "который час? ",
    "ваш кумир детства? ",
    "чем занимаетесь? ",
    "любимый персонаж? ",
    "любимый жанр кино ",
    "влюблены? ",]

rnd1 = randint(0, len(question) - 1)
rnd2 = randint(0, len(question) - 1)
def rand_quest():
    if rnd1 == rnd2:
        rnd2 = randint(0, len(question) - 1)
        return rand_quest()
    return

answ = input(question[rnd1])
answ2 = input(question[rnd2])

fansw = f"{name}, {question[rnd1]} {answ}"
fansw2 = f"{name}, {question[rnd2]} {answ2}"

file = open("quiz.csv", "a")
file.write(f"{fansw}\n")
file.write(f"{fansw2}\n")
file.close()

file = open("quiz.csv", "r")
for row in file:
    print(row)
