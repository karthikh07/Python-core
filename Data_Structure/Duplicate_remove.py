#---------------------------for loop---------------------
l=[1,2,3,4,3,2,4,6,8,1]
res=l.copy()
for a in range(0,len(l)):
    for b in range(a+1,len(l)):
        if l[a] == l[b]:
            res.pop(b)
print('\n')
print(res)
l = res
print('l:',l)

# #----------------while loop working-------------------------
# lt=[1,2,3,4,3,2,4,6,8,1,1]
#
# index = 0
# while index < len(lt):
#     in2 = index + 1
#     while in2 < len(lt):
#         if lt[index] == lt[in2]:
#             lt.pop(in2)
#             in2 -=1
#         in2 += 1
#     index += 1
# print(lt)
