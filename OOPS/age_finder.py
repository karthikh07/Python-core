from datetime import date
class person:

    def __init__(self,name,year):
        self.name = name
        self.year = year

    # @staticmethod
    def age(self):
        age=date.today().year-self.year
        return age

    # @classmethod
    def _check(self):
        age1 = person.age(self)
        if age1>=18:
            print('%s is a Adult'%self.name)
        else:
            print('\n%s is a not Adult\n'%self.name)

k=person('roy',2009)
k._check()
