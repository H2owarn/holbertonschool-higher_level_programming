#!/usr/bin/python3
"""This module write Write a class BaseGeometry and Square classes"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class for Square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size
