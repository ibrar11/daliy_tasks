li = [24,25,30,10,5,15,67,45]

filtration = lambda nums:[num for num in nums if num%5 == 0]
print(filtration(li))