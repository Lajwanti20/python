

#print a number between 1 - 20 using for and range()

print("Print all number")
for i in range(1,20,1):
    print(i)

#print a even number between 1 - 20 using for and range()
print("Print even number")
for i in range(2,21,2):
    print(i)

#print a number between 1 - 50 using for and range() and print a name when number is multiple of 5.

print("Print all number")
for i in range(1,51,1):
    if(i % 5 == 0):
        print("Python Language")
    else:
        print(i)    

#print a sqaure number using a for loop.
numList = [1,2,3,4,5,6,7,8,9,10]
for square in numList : 
    print("Sqaure:",square**2)
