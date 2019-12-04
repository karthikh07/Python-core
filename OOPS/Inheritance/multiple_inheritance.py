class A:
    def sides(s):
        print('three sides')

class B():
    def sides(s):
        print('4 sides')


class penta():
    def sides(s):
        print('5 sides')


class C(A,B):
    def sides(s):
        print('demo sides')

class D(C):

    def sides(s):
        super(C,s).sides()
        super(D,s).sides()
        print('sub2 sides')

k=D()
# k.func()
# k.sides()
# k.sides1()
k.sides()
# k.fun2()
# q=three()
# k.sides()









#
#
#
# class three():
#     def sides(s):
#         print('three sides')
#
# class quad():
#     def sides(s):
#         print('4 sides')
#
#
# class penta():
#     def sides(s):
#         print('5 sides')
#
#
# x=200
#
# if x==20:
#     class demo(quad):
#         def func(s):
#             print('demo')
#
# else:
#     class demo(penta):
#         def func(s):
#             print('demo')
#
#
# k=demo()
# k.sides()
