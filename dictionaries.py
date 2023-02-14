ages = {'key': 'value'}
print(ages)
ages = {'kevin': 59, 'alex': 29, 'bob': 40}
print(ages)
print(ages['kevin'])
ages['kayla'] = 21
print(ages)
ages['kevin'] = 60
print(ages)
del ages['kevin']
print(ages)
# del ages
# print(ages)  # Error

print('kevin' in ages)
print('kayla' in ages)

# alternative syntax for key-value pairs
weights = dict(kevin=160, bob=240, kayla=135)
print(weights)

# initialize a dict with list of tuples
colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
print(colors)

