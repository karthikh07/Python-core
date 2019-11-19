class atm:
    """docstring for atm."""
    bal = 2000

    def __init__(self, pin):
        self.pin = pin


    def security(self):
        z=8888

        if self.pin==z:
            print('cor pin')
            atm.banking()

        else:
            print('wrong pin')

    def banking():
        print('enter your choice')
        key = int(input())
        if key == 1:
            atm.withdraw()
            print(atm.bal)
        elif key == 2:
            atm.deposit()
        elif key==3:
            atm.balance()
        elif key==4:
            atm.exit()
        else:
            print('enter valid key')

    def withdraw():
        print('enter amount to  withdraw')
        amt = float(input())
        if atm.bal <= amt:
            print('insufficient fund')

        elif amt<100:
            print('min balance to withdraw is 100')

        else:
            atm.bal =  atm.bal - amt
            print('%d withdrawn from account'%amt)
            print('balance',atm.bal)

    def deposit():
        print()
    def balance():
        print()
    def exit():
        print()






p = atm(int(input()))
p.security()
