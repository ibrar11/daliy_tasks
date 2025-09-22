marksInSub1 = int(input("Enter marks in subject 1: "))
marksInSub2 = int(input("Enter marks in subject 2: "))
marksInSub3 = int(input("Enter marks in subject 3: "))

totalMarks = marksInSub1 + marksInSub2 + marksInSub3
percentage = (totalMarks / 300) * 100
per1 = (marksInSub1 / 100) * 100
per2 = (marksInSub2 / 100) * 100
per3 = (marksInSub3 / 100) * 100

if (percentage >= 40 and per1 >= 33 and per2 >= 33 and per3 >= 33):
    print("You are passed")
else:
    print("You are failed")