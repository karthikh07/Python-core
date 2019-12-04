from abc import ABC, abstractmethod

class Test(ABC):
    def sides(self):
        pass

class three:
    def sides(s):
        print('three sides')

class quad():
    def sides(s):
        print('4 sides')


class penta():
    def sides(s):
        print('5 sides')


class demo(three,quad,penta):
    def func(s):
        print('demo')

k=three()
k.sides()

p=penta()
p.sides()

d=demo()
d.sides()
d.func()
