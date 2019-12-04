

#----------------while loop working-------------------------



lt = []
def dup():

    lt = list(a)
    index = 0
    while index < len(lt):
        in2 = index + 1
        while in2 < len(lt):
            if lt[index] == lt[in2]:
                lt.pop(in2)
                in2 -=1
            in2 += 1
        index += 1

    return lt

a=(input('enter a list'))
dup()
print(lt)
