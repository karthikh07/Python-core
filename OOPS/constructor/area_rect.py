class rect():
    def __init__(self,sideA,sideB,sideC):
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC

    def area(self):
        return self.sideA * self.sideB

    def solid(self):
        return self.sideA * self.sideB * self.sideC

r1 = rect(10,4,8)

print(r1.sideA,r1.sideB)
print(r1.area())
print(r1.solid())
