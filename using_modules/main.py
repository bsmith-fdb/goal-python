#!/usr/bin/env python
# import helpers
# import helpers as foo
# from helpers import extract_lower, extract_upper
# print("Importing helpers from main")
# from helpers import extract_lower  # the name is hidden from import *
# from helpers import _private_function

# from helpers import extract_lower, extract_upper  # , _private_function

# print("Importing extras from main")

# print(f"__name__ in main.py: {__name__}")

if __name__ == "__main__":
    print(f"Lowercase letters: {extract_lower(name)}")
    print(f"Uppercase letters: {extract_upper(name)}")
    _private_function()
