b = b'This is a bytes'
print(b)
b = bytes(10)
print(b)
b = bytes(range(12))
print(b)
print(b[0])
print(b[0:1])

ba = bytearray()
print(ba)
ba = bytearray(10)
print(ba)
ba = bytearray(range(12))
print(ba)
ba[0:1] = b't'
print(ba)
ba[0] = 0xff
print(ba)

with open('cars.txt', 'rb') as my_file:
    print(my_file.read())
    my_file.seek(0)
    print(my_file.readlines())

with open('cars.txt', 'rb') as my_file:
    ba = bytearray(10)
    my_file.readinto(ba)
    print(ba)

with open('cars.txt', 'rb') as my_file:
    ba = bytearray(my_file.read(5))
    print(ba)