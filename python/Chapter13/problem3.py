# List containing multiplication table of 7
table_of_7 = [7 * i for i in range(1, 11)]

# Convert list elements to a vertical string
vertical_string = "\n".join(str(num) for num in table_of_7)

# Print the result
print(vertical_string)
