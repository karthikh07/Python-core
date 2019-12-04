#------------normal data is immutable-----------#

def fun(l):
    l+='welcome'
    print(l)

l='hi'
print(l)
fun(l)
print(l)

# #----------------list is mutable-----------------#
# def fun(l):
#     l.append(20)
#     l.append(20)
#     print(l)
#
# l=[1,2,3]
# print(l)
# fun(l)
# print(l)
