from time import sleep
from random import randint

a = randint(0, 100)
print("\nПривет, угадай число от 0 до 100 за 10 попыток!\n")

sleep(2)


def ugadayka(rand, count):
  print(f"\nТекущая попытка: {count + 1}")
  b = int(input("Введите число: "))
  if count < 9:
    if b == rand:
      print(f"\nТы угадал число c {count + 1} попытки!")
    if b < rand:
      print("Число больше, чем ты предположил, попробуй еще раз \n")
      return ugadayka(rand, count + 1)
    if b > rand:
      print("Число меньше, чем ты предположил, попробуй еще раз \n")
      return ugadayka(rand, count + 1)
  else:
    print(f"\nВы не угадали за 10 попыток, число было {rand}")


ugadayka(a, 0)