words_to_censor = ["Donkey", "badword", "stupid"]

with open("data.txt", "r") as f:
    content = f.read()

for word in words_to_censor:
    content = content.replace(word, "#####")

with open("data.txt", "w") as f:
    f.write(content)

print("All unwanted words have been censored ✅")
