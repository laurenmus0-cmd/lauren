#elif-used to test multiple conditions
"""

if..elif..else
if condition1:
    block of code to be executed if condition1 is true
elif conditio2:
    block of code to executed if condition2 is true
else:
    block of code to be executed if all conditions are false
"""
#a program that asks user for marks then prints the grade
#80-100-A
#70-80-B
#60-70-C
#50-60-D
#ELSE FAIL
marks=int(input("enter your marks"))
if marks>=80 and marks<=100:
    print("GRADE A")
elif marks>=70 and marks<80:
    print("GRADE B")
elif marks>=60 and marks<70:
    print("GRADE C")
elif marks>=50 and marks<60:
    print("GRADE D")
else:
    print("FAIL")
#a program that asks user and prints
#18-30-young adult
#30-45-adult
#45-65-mature adult
#65-100-elderly
#<18-baby
age=int(input("enter your age"))
if age>=65 and age<=100:
    print("ELDERLY")
elif age>=45 and age<65:
    print("MATURE ADULT")
elif age>=30 and age<45:
    print("ADULT")
elif age>=18 and age<30:
    print("YOUNG ADULT")
else:
    print("BABY")