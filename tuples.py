point = (2.0, 3.0)
print(point)
print(point[0])
print(point[1])
# point[0] = 4.0  # immutable
print(id(point))
point += (4.0,)  # append to tuple
print(id(point))  # new memory allocated
print(point)
x, y, z = point
print(x)
print(y)
print(z)
print("My name is %s %s" % ("Ben", "Smith"))  # unpack a tuple

# tuples versus lists
# use tuples when you know how many items, otherwise use list
# tuples: return multiple pieces of info from a function
# ex: name, age, phone number
# person = ('Kevin Bacon', 61, '555-555-5555')

# embed a list inside a tuple
my_list = [1, 2, 3]
my_tuple = (my_list, 1)
print(my_tuple)
my_list.append(0)
print(my_tuple)


