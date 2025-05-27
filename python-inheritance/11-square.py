#!/usr/bin/python3
"""This module write Write a class BaseGeometry and Square classes"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class for Square"""

    def __init__(self, size):
        """Initializes a square using Rectangle's initialization."""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ return the square description"""
        return f"[Square] {self.__size}/{self.__size}"
