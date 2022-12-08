class Cloth:
  pass


class Coat(Cloth):
  reversed = ''

  def __init__(self, V):
    self.V = V
    Coat.reversed = self.V / 6.5 + 0.5
    self.__its = self.V / 6.5 + 0.5

  @property
  def its(self):
    return self.__its


class Suit(Cloth):
  reversed = ''

  def __init__(self, H):
    self.H = H
    Suit.reversed = self.H * 2 + 0.3
    self.__its = self.H * 2 + 0.3

  @property
  def its(self):
    return self.__its


suit = Suit(5)
coat = Coat(54)

print(Coat.reversed)
print(Suit.reversed)
