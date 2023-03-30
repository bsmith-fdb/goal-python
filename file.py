my_file = open('cars.txt', 'w+')
my_file.write('Mazda6\n')
my_file.write('Ferrari\n')
my_file.writelines(['Honda\n', 'Toyota\n'])
my_file.seek(0)
my_file.write('00000')
my_file.seek(0)
print(my_file.read())
my_file.close()

# my_file = open('cars.txt', 'r')
# print(my_file.read())
# my_file.close()

with open('cars.txt', 'w+') as my_file:
    my_file.write('foo\n')
    my_file.write('bar\n')

with open('cars.txt', 'r') as my_file:
    for line in my_file.readlines():
        print(line)