#inheritance a child class inherits attributes and method from parent
#super/parent class
class Animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def speak(self):
        return f'hello'
    def supermethod(self):
        return f'hello form a method in super class'
#child/sub class
class Dog(Animal):
    def speak(self):
        return f'bark bark'
    def chrome(self):
        return f'hello from a method in dog class'
#add ca class cat that inherite from a animal
class Cat(Animal):
    def speak(self):
        return f'meow meow'
#create a dog object
mydog = Dog("Selina",18)
#create a cat object
mycat = Cat("nany",22)
print(mydog.name)
#call a parent method
print(mydog.supermethod())
#overriding method
print(mydog.speak())
#calling our own method
print(mydog.chrome())
#calling the speak method for a cat
print(mycat.speak())
#calling my cat's name
print(mycat.name)
print(mycat.supermethod())
print(f' My dogs name is {mydog.name} it is {mydog.age} years old and it sounds like {mydog.speak()} ')
print(f' my cats name is {mycat.name} it is {mycat.age} years old and it sounds like {mycat.speak()} ')