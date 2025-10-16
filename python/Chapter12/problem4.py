try:
    numerator = int(input("Enter the numerator: "))
    denumerator = int(input("\nEnter the denumerator: "))
    ans = numerator/denumerator
    print(f"\n{ans}")
except ZeroDivisionError:
    print(f"\ninfinity")
