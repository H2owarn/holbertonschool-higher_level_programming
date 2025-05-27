#!/usr/bin/python3
"""This module write Write a class BaseGeometry"""

#!/usr/bin/python3
"""This module write Write a class BaseGeometry"""


class BaseGeometry:
    """A class for geometric operations."""

    def area(self):
        """Raises an exception since area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if the given value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """A class for Rectangle"""

    def __init__(self, width, height):
        self.integer_validator(width, width)
        self.integer_validator(height, height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
