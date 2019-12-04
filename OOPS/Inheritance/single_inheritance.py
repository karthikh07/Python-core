class A:
    a=20
    b=40

    def multi(self):
        print(self.a*self.b)

class B(A):
    x=20
    y=20

    def add(self):
        print(self.x+self.y)

k=B()
k.add()
k.multi()
