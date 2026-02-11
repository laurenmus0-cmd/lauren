#function-perform a specific task
"""
def functionname():
    block of code
"""
def demo():
    print("good afternoon")
#calling the function
demo()
demo()
#another function
def greetings(name):
    print("wassup",name)
greetings("kevin")
greetings("mariele")
#a function with multiple parameters
def studentinfo(first_name,last_name,age):
    print(f"hello {first_name} {last_name} are you {age} years old?")
#calling the function
studentinfo("kelvin","klein",18)
studentinfo("mariele","mariele",18)
#function that can calculate the are of a triangle
def areaofrectangle(width,height):
    area=width*height
    print(f"the area of a rectangle with {width} and {height} is {area}")
#calling the function
areaofrectangle(17890,20)
areaofrectangle(10,200000)
#a function that calculates the area of a circle p.i=3.14 r*r
def areaofcc(radius,pi=3.14):
    area=pi*radius**2
    print(f"the area of a circle of radius {radius} is {area}")
areaofcc(1000)
areaofcc(155)