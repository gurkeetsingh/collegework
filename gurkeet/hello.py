import numbers
import random
rand=random.randint(1,100)
guess=0
number=0

while(rand!=number):
    number=int(input("enter your guess:"))
    guess+=1
    if(rand==number):
        print(f"congrats you guessed this right in {guess} guesses")
    else:
        if(rand>number):
            print("your guess is smaller")
        else:
            print("your guess is large")

