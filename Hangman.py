import random as rdm
import string 

words=['encyclopedia','keyboard']

#returns the updated word with dashes updated.
def replacer(char,word,index_list):
    for i in index_list:

        new_word=word[:i*2]+char+word[(i*2)+1:]
        word=new_word
    return word

#gets the indices of letters to be replaced.
def index_getter(char,word):
    pos=[i for i,value in enumerate(word) if value==char]
    return pos


def hangman(word):

    #prints the word in the form of dashes.
    def dasher(word):                  
        dash=[]
        length=len(word)
        for dummy in range(0,length):
            dash.append("_")
    
        dashes=",".join(dash)
        return dashes

    print(word)
    tries=6
    dashes=dasher(word)
    print(dashes)

    while tries>0:
        guess=input("input a character..\n")
        if guess in word:
            print("\nGood Job! you guessed right.The updated word is.\n")
            indexes=index_getter(guess,word)
            updated_word=replacer(guess,dashes,indexes)
            dashes=updated_word
            print(updated_word)
            if '_' not in updated_word:
                print("Congratulations! You won.")
                check=input("\nEnter 0 to play again or press enter to exit.")
                if check=='0':
                    hangman(rdm.choice(words))
                else:
                    exit()


        else:
            print("\nSorry, that letter isnt in the word.")
            tries-=1
            print("\nYou have "+str(tries)+" tries left.")

    print("\nSorry Youve run out of tries. Better luck next time.")
    check=input("\nEnter 0 to play again or press enter to exit.")
    if check=='0':
        hangman(rdm.choice(words))
    else:
        exit()

hangman(rdm.choice(words))


#x=input("Input a character..\n")
#print(replacer(x,dashes,z))
