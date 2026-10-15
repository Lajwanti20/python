#Conditional Statements

marks = int(input("Enter your marks:"))
print('Your entered the marks: ',marks)

if marks>= 90 :
    print("YOU HAVE PASSED AND YOU GOT A+ GRADE")
elif (marks >40 and marks <=90):
    print('YOU HAVE PASSED!')

else :
    print("YOU FAILED!")