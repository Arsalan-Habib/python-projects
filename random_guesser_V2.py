import random

def random_guesser():
	
	tries=1
	z=random.randint(1,10)
	x=int(input("\nEnter a number from 1 till 10\n"))
	win=False


	while win==False:
		
		if x==z:
			print("\nMubarak Ho! Tussi Jeet Gaye Janab\nIt took you only "+str(tries)+" tries.")
			check=int(input("\nPress 0 if you want to play again or press enter to exit.\n"))
			if check==0:
				win==True
				random_guesser()
			else:
				exit()
		elif x>z:
			x=int(input("\nThe number you entered was higher than the number i'm thinking of.\nPlease enter a number between 1 and 10 again.\n"))
			tries+=1

		elif x<z:
			x=int(input("\nThe number you entered was lower than the number i'm thinking of.\nPlease enter a number between 1 and 10 again.\n"))
			tries+=1

random_guesser()