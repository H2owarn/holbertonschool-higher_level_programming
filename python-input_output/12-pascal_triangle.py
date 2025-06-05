#!/usr/bin/python3
"""This module returns a list of lists of integers"""


def pascal_triangle(n):
    """Return list of lists"""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # first element is always 1

        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
