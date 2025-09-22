marks = input("Enter marks: ")
totatlMarks = input("Enter total marks: ")

percentage = (float(marks) / float(totatlMarks)) * 100

if percentage >= 90:
    print("Grade Ex")
elif percentage >= 80:
    print("Grade A")
elif percentage >= 70:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 50:
    print("Grade D")
else:
    print("Grade F")