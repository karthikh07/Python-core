try:
    age=14

    if age<17:
        raise ValueError
    else:
        print(age)



except (ArithmeticError,ValueError,IOError):
    print('exception called')

else:
    a=10
    b=20
    print(a+b)
