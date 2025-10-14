class  Calculator:

    def findSq (self, num):
        print(f"Square of {num} is {num * num}")
    
    def findCube (self, num): 
        print(f"Cube of {num} is {num * num * num}")

    def findSqRt (self, num):
        print(f"Squre root of {num} is {pow(num, 0.5)}")

cal = Calculator()
cal.findSqRt(4)
cal.findSq(4)
cal.findCube(4)