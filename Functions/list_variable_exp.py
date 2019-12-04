def fun(*args):
    # print(args)
    num=65
    for i in args:
        x = chr(num)
        print(x,'=',i)
        num+=1



fun(1,2,3,4,5,6,7,8,7,5,4,3,2,5,6,7,4)
