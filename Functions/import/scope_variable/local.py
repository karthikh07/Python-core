name='India'
print('1',name)

def home():
    # global name
    # print('2',name)

    name='bharat'
    print('3',name)

    def hind():
        # nonlocal name
        # print('4',name)

        # global name
        # print('2',name)

        name='hindustan'
        print('5',name)
        def hind1():
            nonlocal name
            print('4',name)

            # global name
            # print('2',name)

            name='hindustan1'
            print('5',name)
        hind1()
        print('3rd',name)
    hind()
    print(name)

home()
print('6',name)
