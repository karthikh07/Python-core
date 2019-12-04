mat1 = []
mat2 = []
tempm1=[]
print('Addition of matrix')
rows1 = int(input('Enter number of rows1: '))
colm1 = int(input('Enter number of colm1: '))
rows2 = int(input('Enter number of rows2: '))
colm2 = int(input('Enter number of colm2: '))
if rows1==rows2 and colm1==colm2:
    for a1 in range(rows1):
        for b1 in range(colm1):
            print('Enter input for matrix 1 for [%d] [%d]'%(a1,b1))
            in1 = int(input())
            tempm1.append(in1)
        tempc = tempm1.copy()
        mat1.append(tempc)
        tempm1.clear()

    for a1 in range(rows2):
        for b1 in range(colm2):
            print('Enter input for matrix 2 for [%d] [%d]'%(a1,b1))
            in1 = int(input())
            tempm1.append(in1)
        tempc = tempm1.copy()
        mat2.append(tempc)
        tempm1.clear()
    print('\nMatrix1: ',mat1)
    print('Matrix2: ',mat2)



    res2=[]
    temp=[]

    for x1 in range(rows1):
        res=[]
        for y1 in range(colm1):
            res.append(mat1[x1][y1] + mat2[x1][y1])
        temp = res.copy()
        res2.append(temp)

    print('Result : ',res2)
    print('\nMatrix:')
    for innerlist in res2:
        print(innerlist)
#         for num in innerlist:
#             print(num,end=' ')
#             print()
else:
    print('Rows and Columns are not equal for Addition of matrix')










print('\n \n \n \n \n \n \n \n \n \n \n \n')
