from functools import reduce

max = lambda a,b: a if a > b else b
val = reduce(max,[43,3,5,34,6])
print(val)