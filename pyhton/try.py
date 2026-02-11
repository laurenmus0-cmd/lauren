"""
try:
  block ofr code that can cause error

except:
  CODE THAT RUNS IF ERROR OCCURS
"""
try:
    num=int(input("Enter a number"))
    print(10/num)
except:
    print("you cannot divide a number by zero")

#another example