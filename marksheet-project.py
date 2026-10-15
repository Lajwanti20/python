#Mini Project : Create a student marksheet with using loop.

#take input a marks from user
marks1 = float(input("Enter marks 1:"))
marks2 = float(input("Enter marks 2:"))
marks3 = float(input("Enter marks 3:"))
marks4 = float(input("Enter marks 4:"))
marks5 = float(input("Enter marks 5:"))

#total marks
totalMarks = 500
print("Total marks is:", totalMarks)
#obtain marks
obtainMarks = marks1+marks2+marks3+marks4+marks5
print("Obtain marks is:", obtainMarks)
#percentage
percentage = (obtainMarks/totalMarks)*100
print("Percentage marks is:", percentage)

if percentage >= 80:
    print("Grade: A+")
elif percentage >= 70:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")


