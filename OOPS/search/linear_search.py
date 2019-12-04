p=[2,3,4,67,21,44,53,45,57,56,63]
print(p)

find1=53
for c in range(len(p),0,-1):
    print(c)
    if find1==p[c]:
        print('element found in index:',c)
        break
