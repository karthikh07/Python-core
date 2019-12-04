class A():
    a=40
    b=20

    def area(self):
        return self.a*self.b

    @classmethod
    def func(cls,a,b):
        cls.a=a
        cls.b=b

    def __repr__(self):
        return 'a={self.a} and b={self.b}'
