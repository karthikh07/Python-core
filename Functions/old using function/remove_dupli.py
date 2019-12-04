# l=[1,2,1,3,4,4,3,5,5,6,8]
# res=l.copy()
# for a in range(len(l)):
#     for b in range(a+1,len(l)):
#         if l[a] == l[b]:
#             res.pop(a)
# print('\n')
# print(l)
# print(res)
# l = res


l=[1,2,3,5,3,6,3,2,1,1]

index = 0
while index < len(l):
    in2 = index + 1
    while in2 < len(l):
        if l[index] == l[in2]:
            l.pop(in2)
            in2 -=1
        in2 += 1
    index += 1
print(l)
