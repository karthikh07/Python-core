
lines=[2,4,6,7,3]
for i in range(len(lines)):
    # print(i)
    f1=open('test.txt','r')
    count=0
    for a in f1:
        x=lines[i]
        # print('line no: ',x)
        count+=1
        # print('count:',count)
        if count==x:
            print(a,end='')
            break










# f1=open('test.txt','r')
#
# count=0
# for i in range(1,20):
#     count+=1
#     # print(count)
#
#     if i==3 or i==2 or i==4  or i==7 :
#         x=f1.readline()
#         # print('if loop',f1.readline(),end='')
#         f2.write(x)
#         continue
#     f1.readline()
