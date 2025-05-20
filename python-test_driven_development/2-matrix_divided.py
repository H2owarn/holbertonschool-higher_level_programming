#!/usr/bin/python3
"""This module provides a function to divide a matrix by a number."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with elements divided by `div`, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """

    # Validate matrix is a list of lists of numbers
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate all rows are the same length
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Return new matrix
    return [[round(num / div, 2) for num in row] for row in matrix]
