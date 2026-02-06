#dictionary-stores data in key:value pairs
student={
    "name":"mary",
    "age":17,
    "course":"mit"
}
print(student)
print(type(student))
#accessing the value
print(student["name"])
print(student["age"])
#adding key:value
student["city"]="nairobi"
print(student)
#updating a value
student["course"]="cyber security"
print(student)
#accessing all keys.#keys()
print(student.keys())
#values()
print(student.values())
#items()
print(student.items())
#loop through all the keys
for key,value in student.items():
    print(key)
    print(value)
#loop through all the values
#loop through all items
for x,y in student.items():
    print(x,":",y)
