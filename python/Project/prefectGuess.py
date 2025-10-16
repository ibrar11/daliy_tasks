import random

num = random.randint(0,100)
guessNum = 1

print("Welcome to the perfect guess game between 0 and 100.")
enteredNum = int(input("\nEnter your to make a guess: "))

while num != enteredNum:
    if(enteredNum < num):
        enteredNum = int(input("Entered number is low. Enter again"))
    elif(enteredNum > num):
        enteredNum = int(input("Entered number is high. Enter again"))

    guessNum += 1

print(f"{guessNum} guesses are used")
