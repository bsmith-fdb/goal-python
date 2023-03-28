# manipulating the "from helpers import *"
__all__ = ['extract_upper']  # will hide for * import. can still be imported explicitly


def _private_function():  # name begins with underscore. it's hidden. must import explicitly
    print("foo")


def extract_upper(phrase):
    return list(filter(str.isupper, phrase))


def extract_lower(phrase):
    return list(filter(str.islower, phrase))


# print(f"__name__ in helpers.py: {__name__}")


# runs once, the first time it's imported
if __name__ == "__main__":
    print("Hello from helpers")

# run a module on cmd line: python -m helpers
