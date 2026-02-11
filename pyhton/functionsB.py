#FUNCTION WITH RETURN KEYWORD RETURN A VALUE

#function that adds two numbers
def addtwonumbers(a,b):
    sum=a=+b
    return sum
#calling the function
result=addtwonumbers(30,50)
print("The sum is",result)
#way two
print(addtwonumbers(55,60))
#function that multiplies 3 numbers
def multiply(a,b,c):
    return a*b*c
result=multiply(10,20,30)
print("The multiplication is",result)
#function that  checks if a number is even or odd
def numbers(a):
    if a%2==0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")
result=numbers(10)
numbers(20)
#get user input
num=int(input("enter a number to check if it is even or odd"))
#calling the function
numbers(num)
#function that finds maximum of the numbers
def max(a,b):
    if a>b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")
max=max(10,20)