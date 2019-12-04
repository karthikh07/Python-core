class atm:
    """docstring for atm."""
    i=1     #transaction fail attempts
    j=1     #pin attempts
    bal = 80000.00  #innitial balance

    def __init__(self, pin):
        self.pin = pin

    def security(self):
        z=int(8888)          # ATM pin

        if self.pin==z:
            print('\n--------------Welcome to Python Bank---------------')
            atm.banking()

        else:
            if atm.j<=3:
                print('wrong pin, attempts left:',3-atm.j)
                print('\n')
                atm.j+=1
                start()
            else:
                print('\n')
                print('----------Your ATM card is locked plz contact Karthik for pin----------')

    def banking():
        print('\nEnter type of transaction')

        key = int(input('---> 1 withdrawal\n---> 2 Deposit\n---> 3 Balacne\n---> 4 Exit\nEnter the  transaction number:  '))
        if key == 1:
            atm.withdraw()
        elif key == 2:
            atm.deposit()
        elif key==3:
            atm.balance()
        elif key==4:
            atm.exit()
        else:
            print('\n')
            if atm.i<=3:
                print('invalid key, attempts left:',3-atm.i)
                atm.i+=1
                atm.banking()
            else:
                print('---------maximum limit exceeded----------')
                atm.exit()


    def withdraw():
        atmbal=40000
        print('\n')
        amt = float(input('enter amount to  withdraw: '))
        if atm.bal <= amt:
            print('\n')
            print('insufficient fund')

        elif amt<100:
            print('\n')
            print('min balance to withdraw is 100')

        elif amt >= atmbal:
            print('\n')
            print('not enough cash in ATM')

        elif amt > 20000:
            print('\n')
            print('20000 is a day limit')

        else:
            atm.bal =  atm.bal - amt
            print('\n')
            print('%d withdrawn from account'%amt)
            print('balance',atm.bal)
        atm.retry()

    def deposit():
        print('\n')
        amt = float(input('enter amount to deposit: '))

        if amt<100:
            print('\n')
            print('min balance to deposit is 100')

        else:
            atm.bal =  atm.bal + amt
            print('\n')
            print('%d DEPOSITED to account'%amt)
            print('balance',atm.bal)
        atm.retry()

    def balance():
        print('\n')
        print('balance',atm.bal)
        atm.retry()

    def exit():
        import sys
        print('\n')
        print('-----------------thank you for using ATM--------------')
        sys.exit()

    def retry():
        e = input('\n Press c to continue \n Press n to exit\n (c/n): ')

        if e=='c':
            atm.banking()

        elif e=='n':
            atm.exit()

        else:
            if atm.i<=3:
                print('\n')
                print('invalid key, attempts left:',3-atm.i)
                atm.i+=1
                atm.retry()
            else:
                print('\n')
                print('-----------maximum limit exceeded-------------')
                atm.exit()


def start():
    p = atm(int(input('Enter your ATM card pin: ')))
    p.security()
start()
