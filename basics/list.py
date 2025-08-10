mylist=['black','white','green','beige']

print(mylist)

# slicing

print(mylist[1:3])
print(mylist[1:1])
print(mylist)

# list methods

mylist.append("grey")
print(mylist)
mylist.remove("green")
print(mylist)
mylist.insert(2,"green")
print(mylist)

mylistcopy=mylist.copy()

mylistcopy.append("magenta")
print(mylistcopy)
print(mylist)

# playing--list comprehension

square=[x**2 for x in range(10)]

print(square)