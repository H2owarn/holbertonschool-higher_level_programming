#!/usr/bin/python3
from add_0 import add
if __name__ == "__main__":
    """Print the result of the addition of 1 and 2"""
a = 1
b = 2
print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))