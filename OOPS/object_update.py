class student():
    def __init__(self,Id,name,age):
        self.Id=Id
        self.name=name
        self.age=age

    def display(self):
        print(self.Id,'',self.name,'',self.age,'')

s=student(1,'rock',30)
s.display()

print(getattr(s,'age'))

setattr(s,'age',50)

print(getattr(s,'age'))

print(hasattr(s,'age'))
