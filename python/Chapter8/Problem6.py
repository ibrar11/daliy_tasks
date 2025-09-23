def inches_to_cm(inches):
    return inches * 2.54

inch = float(input("Enter length in inches: "))
cm = inches_to_cm(inch)
print(f"{inch} inches = {cm} cm")
