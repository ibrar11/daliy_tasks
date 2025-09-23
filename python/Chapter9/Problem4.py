with open("data.txt", "r") as f:
    content = f.read()

content = content.replace("Donkey", "#####")

with open("data.txt", "w") as f:
    f.write(content)

print("All 'Donkey' words have been replaced with #####")
