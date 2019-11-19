class test():
    x=20
    y=30
    def disp(self):
        print(self.x)
        print(self.y)
        # print(x)
        # print(y)
        class test2():
            x=20
            y=30
            def disp2(self):
                print('2',self.x)
                print('2',self.y)
k=test()

k2=test2()
k2.disp2()


# k2.disp()
# k2=test()
