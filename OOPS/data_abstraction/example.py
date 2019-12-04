class A(object):
    """docstring fo A."""

    def __init__(self):
        self.a=22
        self._a=23
        self.__a=24

    def display(self):
        print(self.a)
        print(self._a)
        print(self.__a)

obj=A()
print(obj.a)
print(obj._a)
print(obj.__a)
