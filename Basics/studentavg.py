print ('Enter marks of student out of 100')
count = 0
sub1 = int(input('Enter marks of sub1: '))
if sub1<35:
    count=count+1
sub2 = int(input('Enter marks of sub2: '))
if sub2<35:
    count=count+1
sub3 = int(input('Enter marks of sub3: '))
if sub3<35:
    count=count+1
sub4 = int(input('Enter marks of sub4: '))
if sub4<35:
    count=count+1
sub5 = int(input('Enter marks of sub5: '))
if sub5<35:
    count=count+1
sub6 = int(input('Enter marks of sub6: '))
if sub6<35:
    count=count+1

print('___________________________________')
print('------------Marks Sheet------------')
print('marks of Subject 1 : %d '%sub1)
print('marks of Subject 2 : %d '%sub2)
print('marks of Subject 3 : %d '%sub3)
print('marks of Subject 4 : %d '%sub4)
print('marks of Subject 5 : %d '%sub5)
print('marks of Subject 6 : %d '%sub6)
total = sub1+sub2+sub3+sub4+sub5+sub6
print('___________________________________')
print('total is:            %d'%total)



if sub1>35 and sub2>35 and sub3>35 and sub4>35 and sub5>35 and sub6>35:
    if sub1<101 and sub2<101 and sub3<101 and sub4<101 and sub5<101 and sub6<101:
        print('')
        avg = total/6
        print ('average is:          %d'%avg)

        if avg>=80:
            print ('Grade: Distinction')

        elif avg>=60 and avg<80:
            print ('Grade: First class')

        elif avg>=50 and avg<60:
            print ('Grade: Second class')

        elif avg>=35 and avg<50:
            print ('Grade: Pass')

    else:
        print('subject marks should be less than or equal to 100')

else:
    print('')
    print('Grade: Fail')
    print('')
    print('Remarks: Failed %d subjects'%count)
