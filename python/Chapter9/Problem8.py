with open("this.txt", "r") as f:
    content = f.read()

with open("copy.txt", "w") as f:
    f.write(content)

print("File copied successfully from this.txt to copy.txt")
