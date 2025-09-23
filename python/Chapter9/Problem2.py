import random

def game():
    return random.randint(1, 100)

score = game()
print(f"Your score: {score}")

try:
    with open("Hi-score.txt", "r") as f:
        content = f.read().strip()
        if content:
            hi_score = int(content)
        else:
            hi_score = 0
except FileNotFoundError:
    hi_score = 0

if score > hi_score:
    print("New High Score!")
    with open("Hi-score.txt", "w") as f:
        f.write(str(score))
else:
    print(f"High Score remains: {hi_score}")
