#class is a blueprint of creating objects
#object-is an instance of class
#object-attributes and methods
class Employee:
    def __init__(self,first_name,second_name,salary,department):
        self.first_name=first_name
        self.second_name=second_name
        self.salary=salary
        self.department=department

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.salary} {self.department}"
    def annual_salary(self):
        return f"{self.salary * 12}"
    def full_name(self):
        return f"{self.first_name} {self.second_name} "


#create an object
emp1=Employee("John","Doe",5000,"Math")
#create another object
emp2=Employee("Jane","Doe",5000,"software engineering")
#access the attribute value
print(emp1.first_name)
print(emp1.second_name)
print(emp1.salary)
print(emp1.department)
print(emp2.first_name)
print(emp2.second_name)
print(emp2.salary)
print(emp2.department)
#printing first object
print(emp1.salary)
#calling the annual salary()
print(emp1.annual_salary())
print(f'{emp1.full_name()} salary is {emp1.annual_salary()}')
#print second object
print(emp2.full_name())
#calling the annual salary
print(emp2.annual_salary())
print(f'{emp2.full_name()} salary is {emp2.annual_salary()}')
#calling the full name()
print(emp1.full_name())
print(emp2.full_name())