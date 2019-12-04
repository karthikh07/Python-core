# #----------------------find index withot----------------------#
#
# l=[3,1,2,2,2,4,5,7]
# for a in range(len(l)):
#     if l[a]==2:
#         break
# print('index',a)


# #----------------------nested break-------------------------#
# for i in range(1,4):
#     for j in range(1,4):
#         if i==2 and j==2:
#             break
#         print(i,j)
#     print('outer',i,j)

#----------------------nested continue-------------------------#
for i in range(1,4):
    for j in range(1,4):
        if i==2 and j==2:
            continue
        print(i,j)
    print('outer',i,j)
