#list=used to mutiple elements in a single variable
#list is ordered,changeable and allows duplicates
student=["lauren","mary","peter","jane","allison"]
mynum=[78,56,34,56,34]
print(student)
print(mynum)
print(type(student))
print(type(mynum))
#len()-length
print(len(student))
print(len(mynum))
#accessing list item
print(student[0])
print(mynum[3])
#modifying list item
print(student)
student[1]="angela"
print(student)
#list methods,append(),remove(),pop()
#append-adds an item at the end
student.append("john")
print(student)
#remove-removes a specific item
student.remove("allison")
print(student)
#insert()-adds an element at specific index
student.insert(1,"lewis")
print(student)
#looping through a list
for x in student:
    print(x)
#a list of courses
courses=["HTML","CSS","JAVA","BOOTSTRAP","JAVASCRIPT"]
print(courses)
print(courses[3])
courses[3]="PYTHON"
print(courses)
courses.append("BOOTSTRAP")
print(courses)
courses.remove("BOOTSTRAP")
print(courses)
for x in courses:
    print(x)