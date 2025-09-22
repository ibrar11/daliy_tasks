marks = []
count = 6
while (count > 0):
    mark = input("Enter the marks: ")
    marks.append(int(mark))
    count -= 1

marks.sort()
print(marks)