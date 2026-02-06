#tuples are ordered, unchangeable and allows duplicates
courses=("HTML","Python","Java","C++","bootstrap")
print(courses)
print(type(courses))
#accessing the item
print(courses[1])
#len()
print(len(courses))
#loop
for x in courses:
    print(x)
#tuple()
digits=tuple((19,4,34,98,67,45))
print(digits)
print(type(digits))
for y in digits:
    print(y)