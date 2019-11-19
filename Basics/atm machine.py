pin = 9248
bal = 50000
print('start your transaction')
kpin=int(input('enter your pin: '))


while 1:
	if pin!=kpin:
		print('unauthorised')

	else:
		print('\npress 1 for withdrawal.\n Press 2 for account statement.\n Press 3 for Deposit')
		take=int(input())
		if take == 1:

			print('enter amount')
			amt=int(input())
			if bal>=amt:
				print ('you withdrawn %d rupees'%amt)
				bal = bal-amt
				print('your account balance is %d'%bal)
				print('your transaction is sucussfull plz collect your money')
			else:
				print('not enough balance')

		elif take == 2:
	 		print('your account balance is %d'%bal)

		elif take == 3:
			dep = int(input('enter amount to be deposited: '))
			if dep>=100:
				bal = bal+dep
				print('your account balance is %d'%bal)
				print('your transaction is sucussfull')

			else:
				print('min deposit amount is 100')

		else:
			print('wrong key enterd')
	print('\npress y to continue')
	x=input()
	if x=='y':
		continue
	else:
		print('not valid key')
		break
