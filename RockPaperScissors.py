import random

def play():
    user = input("choose 'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(["r","p","s"])
    print(f"computer has chosen {computer}")

    if user == computer:
        print("tie")
    elif user == "r" and computer == "s":
        print("you win")
    elif user == "p" and computer == "r":
        print("you win")
    elif user == "s" and computer == "p":
        print("you win")
    else:
        print("you lose")

play()