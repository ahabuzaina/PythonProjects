import random

from regex import R

def play():
    user = input("choose 'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(["r","p","s"])
    print(f"computer has chosen {computer}")

    if user == computer:
        return "Tie"
    elif user == "r" and computer == "s":
        return "you win"
    elif user == "p" and computer == "r":
        return "you win"
    elif user == "s" and computer == "p":
        return "you win"
    
    return "you lost"

print(play())