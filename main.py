#Write a program to generate a random integer 
#and match it with the input given by the user?
import random
num_user=int(input("Enter any number:"))
y=random.randint(1,5)
print(y)
if num_user==y:
    print("Your number matches the random number. You won the game, congrats!")
else:
    print("Sorry you failed the game.")