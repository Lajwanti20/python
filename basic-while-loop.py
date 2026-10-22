
#print name 100 time using loop

num = 1

while num<=5:
    print("Hello World",num)
    num = num+1

#print a number from 1-10

a = 1
while a<=10:
    print(a)
    a+=1    

print("=====================")

#print a number from 10-1

j = 10
while j>=1:
    print(j)
    j-=1     
print("=====================")


#print even numbers from 1-50

i = 1

while i <= 50:
    if i % 2 == 0:
        print("Even Number:", i)
    i = i + 1

print("=====================")


#sum of first n natural number

sum = 1
result = 0

while sum <= 5:
   
    result = result + sum
    sum = sum + 1
print("Sum:", result)

print("=====================")

#print a star traingle using while loop

star = "*"
k = 1


while k <= 5:
    n = 1
    while n <= k:
        print(star,end="")
        n+=1
    print()    
    k+=1
print("=====================")  
#print a star traingle using a single while loop

star = "*"
k = 1
while k <= 5:
   
        print(star*k)
        k+=1

print("=====================")

#print a star traingle using while loop

star = "*"
k = 1


while k <= 5:
    n = 5
    while n >= k:
        print(star,end="")
        n-=1
    print()    
    k+=1
print("=====================")  

#print a table using while loop

tableNumber= int(input("Enter a table number:"))
result = 0
number = 1
print("Table of ", tableNumber)
while  number <= 10:
    #both are acceptable
   # result = number * tableNumber
    #print(tableNumber, "x" , number ,"=", result)
    print(f"{tableNumber} x {number} = {tableNumber*number}")
    number+=1