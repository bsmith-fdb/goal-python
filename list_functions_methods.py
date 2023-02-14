my_list = [1, 2, 3]
print(my_list)
my_list.append(9)
print(my_list)
my_list.insert(0, 22)
print(my_list)
my_list.sort()  # sort in place
print(my_list)
print(0 in my_list)
print(1 in my_list)
print(0 in my_list or 2 in my_list)
my_list_sorted = sorted(my_list)  # return a new sorted list
my_list_reversed = reversed(my_list)  # return a new reversed list
print(my_list_reversed)
print(list(my_list_reversed))
print(list(reversed(sorted(my_list))))
