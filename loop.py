count = 1
while count <= 4:
    print('looping')
    count += 1

for i in sorted([1, 4, 99, 32]):
    print(i)

for i in range(1, 20, 2):
    print(i)

point = (1, 2, 3)
for p in point:
    print(p)

for key, value in dict(kevin=32, bob=40, kayla=21).items():
    print(key, value, sep=':')

for letter in 'my string':
    print(letter)

for i in range(1, 22):
    if i & 0x1 == 0:
        print(i, 'is even')
    elif i & 0x1 == 1:
        print(i, 'is odd')


for i in [1, 2, 3, 4, 5, 5, 5]:
    print(i)
    break
else:
    print('loop completed')  # executes when the loop did NOT exit early


# list comprehension
print('evens', [i for i in range(1, 22) if i & 0x1 == 0])
print('odds', [i for i in range(1, 22) if i & 0x1 == 1])

fruits = ['apple', 'orange', 'banana', 'grapefruit', 'dragonfruit']
print('contains "a"', [x for x in fruits if 'a' in x])
print('contains "b"', [x for x in fruits if 'b' in x])

uppercase_fruits = [x.upper() for x in fruits]
print(uppercase_fruits)



