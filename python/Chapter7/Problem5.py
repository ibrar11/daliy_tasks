num = int(input("Enter a number: "))
count = 1
sum = 0

while count <= num:
    sum += count
    count += 1

print("The sum of the first", num, "natural numbers is:", sum)