import random
import sys

print(BaseException.__bases__)
print(BaseException.__subclasses__())
print(Exception.__subclasses__())
print(Exception.__bases__)
print(IndexError.__subclasses__())
print(IndexError.__bases__)
exit(0)

try:
    print(f"received argument {sys.argv[0]}")
    random.shuffle(sys.args)
except (IndexError, NameError) as err:  # catch multiple types of exceptions
    print(f"handling IndexError, NameError: {err}")
except NameError as err:  # catch a single type of exception
    print(f"handling NameError {err}")
except Exception as err:  # catch any exception, not good practice
    print(f"General exception handler {err}")
else:  # no exception happened
    print("hit else block")
finally:  # always execute
    print(f"Hit finally block")
