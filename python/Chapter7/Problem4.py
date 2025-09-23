num = int(input ("Enter a number: "))
sqRoot = pow(num, 0.5)
count = 2

while count <= sqRoot:
    if num % count == 0:
        print ("Not Prime")
        break;
    count += 1