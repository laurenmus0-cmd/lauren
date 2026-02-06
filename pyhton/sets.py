#sets-are unordered,unchangeable and do not allow duplicates
rooms={"chrome","moxilla","brave","safari"}
print(rooms)
print(type(rooms))
#lem()
print(len(rooms))
for x in rooms:
    print(x)
rooms.remove("moxilla")
print(rooms)
