from time import sleep

class Trafficlight:
    def __init__(self, color):
        self.color = color

    def red(self):
        sleep(1)
        print("Красный")

    def orange(self):
        sleep(0.5)
        print("Оранжевый")

    def green(self):
        sleep(2)
        print("Зелёный")

r = Trafficlight('Красный')
o = Trafficlight('Оранжевый')
g = Trafficlight('Зелёный')
print("Светофор")
r.red()
o.orange()
g.green()
r.red()