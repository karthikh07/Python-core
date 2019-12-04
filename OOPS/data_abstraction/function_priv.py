class A(object):
    """docstring fo A."""

    def __init__(self):
        self.a=22
        self._a=23
        self.__a=24
        A.display(self)

    def display(self):
        print('Disp',self.a)

    def _display(self):
        print('_Disp',self.a)

    def __display(self):
        print('__Disp',self.a)


obj=A()
# obj.display()
# obj._display()
# obj.__display()
