mat1=[[1,2,3],[2,3,4],[5,4,3]]
mat2=[[8,6,2],[1,3,7],[4,3,1]]
res=[]
res2=[]
temp=[]
add=0
i=0

while i<3:
    j=0
    while j<3:
        add = mat1[i][j] + mat2[i][j]
        res.append(add)
        j+=1
    temp=res.copy()
    res2.append(temp)
    res = []
    i+=1

print(res2)
