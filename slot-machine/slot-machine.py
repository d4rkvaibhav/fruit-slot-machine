# coding: utf8	

import random
FRUITS = ['🍌', '🍒', '🍐', '🍈', '🍇', '🍊', '🍉','🥐','🥞',' 🍟','🌭','🥣']
def line():
	return [random.choice(FRUITS) for i in range(3)]

def roll():	
	print("['🍌', '🍒', '🍐', '🍈', '🍇', '🍊', '🍉','🥐','🥞',' 🍟','🌭','🥣']")
	print()
	print("****************************************************************************")
	print('			Welcome to Fruit Slots!')
	print("****************************************************************************")
	print()
	print("['🍌', '🍒', '🍐', '🍈', '🍇', '🍊', '🍉','🥐','🥞',' 🍟','🌭','🥣']")
	print()
	money=random.randint(100,10000)
	print('-------------------You have Rs.',money,' money in your wallet .---------------')
	print()
	print("If you earn more than Rs.100000 you will win this")
	print()
	while True:
		print("---->   Current Money    :",float(money))
		print('---->   Enter your bet   :',end="   ")
		
		bet = input()
		print()
		try:
			bet = float(bet)
		except:
			print('Your bet must be a number!\n')
			return

		if bet <= 0:
			print('Enter valid number !!!!.\n')
			return
		elif bet > money:
			print('You don\'t have enough money to wager this.\n')
			
			return

		line1 = line()
		line2 = line()
		line3 = line()
		if(line2[0]==line2[1]==line2[2]):
			money+=bet
			win=bet
		else:
			win=0
			money-=bet
		print("----------------")
		print('{}\n{} ◀\n{}\n'.format(' : '.join(line1), ' : '.join(line2), ' : '.join(line3)))

		if win > 0:
			print('You won Rs',bet)
		else:
			print('You lost Rs.',bet,' money')

		if money <= 0:
			print('You have no money left. Low roller.\n')
			
			return
		elif money < 1000000000:
			print('Play more to become a high roller!\n')
		
roll()
