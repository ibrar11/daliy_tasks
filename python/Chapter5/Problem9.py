s = {8, 7, 12, "Harry", [1,2]} 
# This will raise an error because lists are unhashable and any other element present in the set cannot be accessed

for item in s:
    print(item)