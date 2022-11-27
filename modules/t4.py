class Car:
    def __init__(self, color, marka, kuzov, speed, korobka):
        self.color = color
        self.marka = marka
        self.kuzov = kuzov
        self.speed = speed
        self.korobka = korobka

    def start(self):
        print('Машина начала движение, скорость = 10 км/ч')
        self.speed = 10

    def stop(self):
        print('Машина остановилась, скорость = 0 км/ч')
        self.speed = 0

    def speed_up(self, i=1):
        self.speed += i
        if self.kuzov == "Грузовик":
            if self.speed > 60:
                print(f'Скорость превышена! Разрешённая скорость 60км/ч. Скорость = {self.speed} км/ч')
            else:
                print(f'скорость = {self.speed} км/ч')
        else:
            if self.speed > 80:
                print(f'Скорость превышена! Разрешённая скорость 80 км/ч. скорость = {self.speed} км/ч')
            else:
                print(f'скорость = {self.speed} км/ч')


    def speed_down(self, i=1):
        if self.speed == 0:
            print('скорость = 0 км/ч')
        else:
            self.speed -= i
            if self.kuzov == "Грузовик":
                if self.speed > 60:
                    print(f'Скорость превышена! Разрешённая скорость 60км/ч. Скорость = {self.speed} км/ч')
                else:
                    print(f'скорость = {self.speed} км/ч')
            else:
                if self.speed > 80:
                    print(f'Скорость превышена! Разрешённая скорость 80 км/ч. скорость = {self.speed} км/ч')
                else:
                    print(f'скорость = {self.speed} км/ч')

    def turn(self):
        print("Поворот направо или налево?")
        povorot = input()
        if povorot == "направо":
            print("Машина повернула направо")
        elif povorot == "налево":
            print("Машина повернула налево")
        else:
            print("Едем прямо")

    def beep(self):
        print('БИБИП')

truck = Car("Белый", "Камаз", "Грузовик","0", "Механическая")
car = Car("Серебристый","Ваз","Хетчбек","0", "Механическая")

print(f"Едем на - {truck.marka}")
truck.start()
truck.speed_up(70)
truck.speed_down(15)
truck.turn()
truck.beep()
truck.stop()

print(f"Едем на - {car.marka}")
car.start()
car.speed_up(80)
car.speed_down(40)
car.beep()
car.turn()
car.stop()