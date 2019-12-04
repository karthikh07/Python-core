p=[2,3,4,67,21,44,53,45,57,56,63]

f=63
p.sort()
print(p)
mid=len(p)//2
# print(mid)


def more():
    for c in range(mid+1,len(p)):
        if f==p[c]:
            print('element found in index:',c)
            break
        # else:
        #     print('element not found')
        elif c==(len(p)-1) and f!=p[c]:
            print('element not found')

def less():
    for c in range(mid):
        if f==p[c]:
            print('element found in index:',c)
            break
        # else:
        #     print('element not found')
        #     break
        elif c==(mid-1) and f!=p[c]:
            print('element not found')


if p[mid]==f:
    print('element found in index:',mid)

elif f<p[mid]:
    less()

else:
    more()
