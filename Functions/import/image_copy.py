f1=open('karthik.jpg','rb')
f2=open('E:/9-JSpiders/Examples/Functions/import/file_handle/k.png','wb')

copy = f1.read()
f2.write(copy)
f2.flush()
f2.close()
f1.close()
print('done')
