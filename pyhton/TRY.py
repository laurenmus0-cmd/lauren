"""
try:
    block of code that can cause error
except:
     #CODE THAT RUNS IF ERROR OCCURS
"""
try:
    num=int(input("enter a number"))
    print(10/num)
except:
    print("you cannot divide a number by zero")
#another example
try:
    print(x)
except NameError:
    print("the variable is not defined")
#another example
try:
    eith open('abcd.txt','r') as x
    print(x.read())
except FileNotFoundError:
    print("fle not found")
