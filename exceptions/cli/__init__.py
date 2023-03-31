import sys

from .errors import ArgumentError


def main():
    # if len(sys.argv) < 2:
    #     raise ArgumentError('too few arguments')
    assert len(sys.argv) >= 2, 'too few arguments'  # only for debugging. when run with -O parameter, it's optimized away
    print(f"Name is {sys.argv[1]}")
