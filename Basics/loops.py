n = int(input('enter Number for factorial: '))
res=1
for fact in range(n,1,-1):
    res = res*fact
print (res)
