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
    result = []

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (float, int):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(round(i/div, 2))
        result.append(new_row)
    return result
