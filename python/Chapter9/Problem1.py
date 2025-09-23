with open("poems.txt", "r") as f:
    text = f.read().lower()


if "twinkle" in text:
    print("Yes, the file contains the word 'twinkle'.")
else:
    print("No, the file does not contain the word 'twinkle'.")
