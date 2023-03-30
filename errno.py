#f = open('fake.txt', 'r')  # FileNotFoundError: [Errno 2] No such file or directory: 'fake.txt'
import errno
import os
print(FileNotFoundError.__bases__)
print(PermissionError.__bases__)

try:
    f = open('fake.txt', 'r')
except OSError as err:
    print(f"[Errno {err.errno} ({errno.errorcode[err.errno]})] {os.strerror(err.errno)}")
    if err.errno == errno.ENOENT:
        print('File not found')
    elif err.errno == errno.EACCES:
        print('Bad permissions')

