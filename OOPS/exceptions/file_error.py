try:
    f1=open('test.txt','r')

except:
    print('no file')

else:
    count=0
    for data in f1:
        count+=1
        print(count)
        # print(f1.readline())
        print(data)

finally:
    print('finally executed')
