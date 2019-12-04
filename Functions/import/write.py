f1=open('E:/9-JSpiders/Examples/Functions/import/file_handle/test.txt','r')
f2=open('E:/9-JSpiders/Examples/Functions/import/file_handle/test3.txt','a')
#s='its created by python'
# =f1.read()

count=0
for i in range(1,20):
    count+=1
    # print(count)

    if i==3 or i==2 or i==4  or i==7 :
        x=f1.readline()
        # print('if loop',f1.readline(),end='')
        f2.write(x)
        continue
    f1.readline()
# f2.write(x)
f2.flush()
f2.close()

print('done')
