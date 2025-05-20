#!/usr/bin/python3
"""This module provides a function to  prints a square with the character # """


def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
    size (int): The size of the square.

    Raises:
    TypeError: If size is not an integer.
    ValueError: If size is negative.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        print("#" * size)
