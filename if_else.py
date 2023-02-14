if 'a' < 'b':
    print("true")
else:
    print("false")


if 'b' < 'b':
    print('first condition is true')
elif 'c' < 'd':
    print('second condition is true')
else:
    print('no condition was true')


name = input('what is your name? ')
if len(name) >= 6:
    print('your name is long')
elif len(name) == 5:
    print('your name is exactly 5 chars')
elif len(name) >= 4:
    print('your name is 4 or more chars')
else:
    print('your name is short')

match len(name):
    case 6:
        print('6')
    case 5:
        print('5')
    case _:
        print('unknown')

if name.lower() == 'ben':
    print(f'Hi, {name}')
else:
    pass  # no op
