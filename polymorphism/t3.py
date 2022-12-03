class Matrix():

    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        for i in range(len(self.lst)):
            lst = []
            for j in range(len(self.lst[i])):
                lst.append(f"{self.lst[i][j]}")
            print("  ". join(lst))
        return " "

    def __add__(self, other):
        BB = []
        for i in range(len(self.lst)):
            lst = []
            oldLst = []
            newLst = []

            for j in range(len(self.lst[i])):
                lst.append(self.lst[i][j])
                oldLst.append(other[i][j])

            for i in range(len(lst)):
                newLst.append(lst[i] + oldLst[i])

            BB.append(newLst)
        return BB


m1 = Matrix([[1,2,3],[4,5,6]])
m2 = Matrix([[6,5,4],[3,2,1]])

m3 = m1 + [[6,5,4],[3,2,1]]
m3 = Matrix(m3)
str(m3)