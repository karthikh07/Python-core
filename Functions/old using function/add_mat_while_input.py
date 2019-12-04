mat1=[]
mat2=[]
mattemp=[]
cpy=[]
var = 0
a = 0
b = 0
while a<3:
    while b<3:
        var = int(input('enter number'))
        mattemp.append(var)
        b+=1
    cpy = mattemp.copy()
    mat1.append(cpy)
    mattemp.clear()
    a+=1
    b=0
a=0
while a<3:
    while b<3:
        var = int(input('enter number\n'))
        mattemp.append(var)
        b+=1
    cpy = mattemp.copy()
    mat2.append(cpy)
    mattemp.clear()
    a+=1
    b=0
print('\nmatrix1: ',mat1)
print('\nmatrix1: ',mat2)
res=[]
res2=[]
temp=[]
add=0
i=0
j=0
while i<3:
    while j<3:
        # print(i)
        # print(j)
        add = mat1[i][j] + mat2[i][j]
        res.append(add)
        # print(res)
        j+=1
    temp=res.copy()
    res2.append(temp)
    res.clear()
    i+=1
    j=0


print('res',res2)
