import random

def computerChoice():
    options = ["snake", "water", "gun"]
    return options[random.randint(0, 2)]

def gameResult (userChoice):
    computer = computerChoice()
    if userChoice == computer:
        return "It's a tie!"
    elif (userChoice == "snake" and computer == "water") or \
         (userChoice == "water" and computer == "gun") or \
         (userChoice == "gun" and computer == "snake"):
        return "You win!"
    else:
        return "Computer wins!"


userChoice = input("Enter your choice (snake, water, gun): ").lower()
print(gameResult(userChoice))