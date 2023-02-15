if 1 < 2:
    x = 5  # global var

while x < 6:
    print(x)
    x += 1

print(x)
'''
sdfsdf
sdfdsf
'''

def set_y():
    y = 12  # local var
    x = 9  # local x shadows global x
    print("local x", x)


set_y()
print(x)
# print(y)  # Error
