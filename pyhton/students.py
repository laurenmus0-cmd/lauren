#CLASS IS A BLUEPRINT FOR CREATING ABJECTS
#object is an uinsance of a class
class Student:
    #constructor
    #runs automatically when an object is created
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    def __str__(self):
        return f"the stuent name is {self.name} and their age is {self.age} and course is {self.course}"
    def get_email(self):
        return f'{self.name}emobilis.ac.ke'

#create an object
#object is an instance of a class
#objectname=classname(values)
student1=Student("jane", 17, "MIT")
student2=Student("kamau", 18, "cybersecurity")
print(student1)
print(student2)
#call our function
print(student1.get_email())
print(student2.get_email())

