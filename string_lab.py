message = input('Enter a message: ')
print(f'First character: {message[0]}')
print(f'Last character: {message[-1]}')
print(f'Middle character: {message[int(len(message)/2)]}')
print(f'Even index characters: {message[::2]}')
print(f'Odd index characters: {message[1::2]}')
print(f'Reversed message: {message[::-1]}')
