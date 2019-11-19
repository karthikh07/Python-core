class temp():
    count=0
    def __init__(self):
        temp.count+=1

obj=temp()
obj2=temp()
obj3=temp()
print(temp.count)
