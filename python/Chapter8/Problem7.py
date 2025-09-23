def remove_and_strip(words, target):
    return [word.strip() for word in words if word.strip() != target]

words = [" apple ", "banana", "  orange ", "apple", " grape "]
target_word = "apple"

result = remove_and_strip(words, target_word)
print(result)
