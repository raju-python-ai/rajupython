import random
print(" Heloo!!...Your Self ")
name=input()
num=random.randint(0,30)
guess=int(input(name + " I am thinking a number between 1 to 30..can you guess what it is? "))

while guess != num:
    if guess < num:
        print(" You need to guess higher..Please try again!! ")
        guess=int(input("Guess the number between 1 to 30: "))
    else:
        print(" You need to guess lower..Please try again!! ")
        guess=int(input(" Guess the number between 1 to 30: "))

print("You guess the number perfectly....")