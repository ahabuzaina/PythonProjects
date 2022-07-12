import random
from scipy import rand

def guess(x):
    wrong = True
    randomNumber = random.randint(1,x)
    guess = 0
    while (wrong):
        guess = int(input(f"guess a number between 1 and {x}"))
        if guess == randomNumber:
            wrong = False
            print("You're too good!")
        elif guess > randomNumber:
            print("too high")
        elif guess < randomNumber:
            print("too low")
    
guess(10)


