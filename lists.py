my_list = []
print(len(my_list))
my_list = ['a']
print(len(my_list))
my_list = [1, 'b', True, 1.111]
print(my_list)
print(my_list[-1])
print(my_list[-2])
print(my_list[1:])
# lists are mutable
print(id(my_list))
my_list.append('foo')
print(id(my_list))
my_list.insert(0, 'bar')
print(my_list)
print(id(my_list))
my_list[2:3] = [2, 3, 5, 5, 5]
print(my_list)
del my_list[0]
print(my_list)


