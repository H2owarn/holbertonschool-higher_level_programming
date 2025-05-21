#!/usr/bin/python3
"""This module write a class Square. """


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        self.__size = size   # private class

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Sets the size of the square with validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2    
