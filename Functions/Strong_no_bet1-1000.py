def facto(c):
    add=0
    fact=1
    # print('num',c)
    for x in range(c,0,-1):
        fact=fact*x
    # print(fact)
    return fact

# def count(a):
#     cnt=0
#     while a:
#         a//=10
#         cnt+=1
#     return cnt

def rem(a):
    amst=0
    while a:
        d1=a//10
        dig1 = a-(d1*10)
        c = dig1
        amst = amst+facto(c)
        a=a//10
    #print(amst)
    return amst


for a in range(100000):
    # a = int(input('enter input\n'))
    m = a
    rem(a)
    res=rem(a)
    # print(res)
    if m==res:
        print('strong number',res)
    # else:
    #     print('not strong number')
