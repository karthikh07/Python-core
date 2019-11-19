mat1=[[1,2,3],[2,3,4],[5,4,3]]
mat2=[[9,6,2],[3,5,7],[4,3,1]]
res=[]
res2=[]
temp=[]

for x1 in range(0,len(mat1)):
    for y1 in range(0,len(mat1)):
        add = mat1[x1][y1] + mat2[x1][y1]
        res.append(add)
    temp = res.copy()
    res2.append(temp)
    res = []

print(res2)
for innerlist in res2:
    print(innerlist)

# #-----------------------shortest way-------------------------#
# mat1=[[1,2,3],[2,3,4],[5,4,3]]
# mat2=[[9,6,2],[3,5,7],[4,3,1]]
# res=[[],[],[]]
#
# for x1 in range(0,len(mat1)):
#     for y1 in range(0,len(mat1)):
#         add = mat1[x1][y1] + mat2[x1][y1]
#         res[x1].append(add)
# print(res)
