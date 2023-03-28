# manipulating the "from helpers import *"
__all__ = ['extract_upper', 'extract_lower']  # will hide for * import. can still be imported explicitly


def _private_function():  # name begins with underscore. it's hidden. must import explicitly
    print("foo")


def extract_upper(phrase):
    """
    takes a string and returns a list containing
    only the uppercase characters from the string.
    >>> extract_upper("Hi There, BOB")
    ['H', 'T', 'B', 'O', 'B']
    """
    return list(filter(str.isupper, phrase))


def extract_lower(phrase):
    return list(filter(str.islower, phrase))


# print(f"__name__ in helpers.py: {__name__}")


# runs once, the first time it's imported
if __name__ == "__main__":
    print("Hello from helpers")

# run a module on cmd line: python -m helpers
