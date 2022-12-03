class Cat:
    def __init__(self, imya, okras, vozrast):
        self.imya = imya
        self.okras = okras
        self.vozrast = vozrast

    def meow(self):
        print(self.imya + ' - Мяу')

    def mur(self):
        print(self.imya + ' - Мур')

    def privet(self):
        print(self.imya + ' - Привет :)')


c = Cat('Snejok', 'White', '4')
# Атрибуты
print(c.imya)
print(c.okras)
print(c.vozrast)
# Методы
c.meow()
c.mur()
c.privet()