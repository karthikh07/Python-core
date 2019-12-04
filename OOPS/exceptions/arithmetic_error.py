try:
    print(10/1)

    

except (ArithmeticError,ValueError,IOError):
    print('divided by zero')

else:
    a=10
    b=20
    print(a+b)
