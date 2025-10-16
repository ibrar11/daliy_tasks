try:
    with (open("Table.txt", "w") as f):
        num = int(input("Enter a number: "))
        multiplicationList = [num*n for n in range(1,11)]
        f.write(str(multiplicationList))
except FileExistsError as error:
    print(error)
