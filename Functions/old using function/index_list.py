asc_list=[5,1,18,35,11,33,108,127,7,9,-67,-6]
#asc_list.sort()
#print(asc_list)
dec_list=[5,1,18,35,11,33,108,127,7,9,-67,-6]
for a in range(0,len(asc_list)):
    for b in range(a+1,len(asc_list)):
        if asc_list[a]>asc_list[b]:
            temp=asc_list[b]
            asc_list[b]=asc_list[a]
            asc_list[a]=temp
print('\nAscending:')
print(asc_list)
print('\nLargest no: ')
print(asc_list[len(asc_list)-1])

for a in range(0,len(dec_list)):
    for b in range(a+1,len(dec_list)):
        if dec_list[a]<dec_list[b]:
            temp=dec_list[b]
            dec_list[b]=dec_list[a]
            dec_list[a]=temp
print('\nDecending:')
print(dec_list)
print('\nSmallest no: ')
print(dec_list[len(dec_list)-1])
