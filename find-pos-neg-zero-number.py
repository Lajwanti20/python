#practice question : Take a number from user and print it is positive, negative or zero.

number = int(input("Enter a number:"))

if(number > 0) :
    print(number,"is positive number")
elif (number < 0) :
    print(number, "is negative number")
elif (number == 0) :
    print(number," you entered")
else:
    print("You entered a wrong number")     