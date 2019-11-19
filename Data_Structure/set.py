l=[2,3,5,7,3,1,8,9,2]
s = set(l)
print(s)
s.add(4)
print(s)
m=list(s)
print(m)

a=[2,3,7,4,5,2,4,8,3,32]
b=[3,7,4]
s1=set(a)
s2=set(b)
print(s1.difference(s2))

# s1.difference_update(s2)
# print(s1)

# s2.discard(10)
# print(s2)

print(s1.intersection(s2))                  #gives intersection elements

print(s1.issubset(s2))                      #checks s1 is subset of s2
print(s1.issuperset(s2))                    #checks s1 is superset of s2

print(s1.isdisjoint(s2))                #non comon element gives true

m1={10,2,6,3,5,6,77,33,10,3,2}
print(type(m1))

m1.pop()                    # removes 1st element
print(m1)
m1.pop()
print(m1)

print(s1.union(s2))

m1.remove(10)
print(m1)
