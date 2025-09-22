nums = list(map(int, input().split()))
greates = nums[0]
length = len(nums)

while length > 0:
    if nums[length-1] > greates:
        greates = nums[length]
    length -= 1

print(greates)