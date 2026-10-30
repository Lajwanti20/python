
#function

def greet():
    print("Hello")

greet()
greet()

def sumFun() :
    a =2
    b = 10
    sum = a + b
    print(f'sum of two numbers : {sum}')

sumFun()

#parameter and argument function
#name fun
def nameFun(name):
    print("Hello",name)

nameFun("Lajwanti")    

#sum fun using args and parameters

#Function Definition with parameters
def sumArgs(a,b):
    
    print("Additon of two numbers:",a + b)

#function calling with arguments
sumArgs(10,20)   


#Default Argument function
def nameGreet(name = "Saumya"):
    print("Hello ",name)

nameGreet()
nameGreet("Riya")


#Return Statement
def add(a,b):
    return a+b

result = add(10,40)
print("Result = ",result)


#sqaure of number using return statement
def sqaure(num):
    return num**2

print(sqaure(3))