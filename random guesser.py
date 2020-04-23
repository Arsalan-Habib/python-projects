import random

y=random.randint(1,10)
tries=1

def guesser(count):
    print("\nEnter a number between 1 and 10.")
    x=int(input())

    if x==y:
        print("\nCongratulations! You guessed it right!")
        print("It took you only "+str(count)+" tries.")
        check=input("\nPress 0 if you want to play again or press enter if you want to exit.")
        if check==0:
            guesser(1)
        else:
            exit


    elif  x>y:
        print("Your guess was higher than the number i'm thinking of.")
        guesser(count+1)
        

    elif  x<y:
        print("Your guess was lower than the number i'm thinking of.")
        guesser(count+1)

guesser(tries)