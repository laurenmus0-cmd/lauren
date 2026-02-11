#module-python file that contains python code, it can have functions, variables
#etc that you want to include in your file
#import the module
import math as fm
import random
import datetime

print(fm.sqrt(25))
print(fm.pi)
print(fm.floor(3.46))
print(fm.ceil(3.46))
#generate int btwn 5-14
print(random.randint(5,14))
#generate random number from 0-1
print(random.random())
#generate current date and time
print(datetime.datetime.now())
x=datetime.datetime.now()
print(x.year)
print(x.month)
print(x.day)

