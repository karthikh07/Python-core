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

class C(B):
    s=1
    def check(self):
        print(self.s)

k=C()
k.add()
k.multi()
