def cube(c):
    c_ans = c**count(a)
    # print('cube',c_ans)
    return c_ans

def count(a):
    cnt=0
    while a:
        a//=10
        cnt+=1
    return cnt

def rem(a):
    amst=0
    while a:
        d1=a//10
        dig1 = a-(d1*10)
        c = dig1
        amst = amst+cube(c)
        a=a//10
    #print(amst)
    return amst



a = int(input('enter input\n'))
m = a
rem(a)
res=rem(a)
print(res)
if m==res:
    print('amstrong')
else:
    print('not amstrong')
