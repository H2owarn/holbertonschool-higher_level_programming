#!/usr/bin/python3
"""This module write Write a class BaseGeometry"""


class BaseGeometry:
    """A class for geometric operations."""

    def area(self):
        """Raises an exception since area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if the given value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
