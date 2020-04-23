import random
import string

length=int(input("Enter the length you would like your password to be.\nIt should be 6 at minimum.\n"))
while length<6:
    length=int(input("Enter a value greater than 5.\n"))

    

alphabets=int(input("Enter the number of letters you would like in the password.\nThe remaining space will be filled using numbers and special characters.\n"))

numbers=length-alphabets

def password_generator(a,n):
    password=[]
    for dummy in range(a):
        password.append(random.choice(string.ascii_letters))
        

    for dummy1 in range(n):
        password.append(random.choice(string.digits+string.punctuation))

    
    random.shuffle(password)
    password="".join(password)
      
    return password
    

print("Your password is \" "+password_generator(alphabets,numbers)+" \".")
input("\nPress Enter to exit.....")
