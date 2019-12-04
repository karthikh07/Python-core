class queue:
    list=[]


    def put(self,element):
        print(element,'is inserted\n')
        queue.list.append(element)

    def get(self):
        e=queue.list.pop(0)
        print(e,'is deleted\n')

    def display(self):
        print('QUEUE:',queue.list,'\n')




d=queue()
d.put(1)
d.display()
d.put(2)
d.display()
d.put(3)
d.display()
d.get()
d.display()




















d.put(4)
d.display()
d.put(5)
d.display()
d.get()
d.display()
d.put(6)
d.display()
d.put(7)
d.display()
d.get()
d.display()
