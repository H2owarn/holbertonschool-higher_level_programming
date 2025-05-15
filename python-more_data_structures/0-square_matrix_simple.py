#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    power = 2
    return [list(map(lambda x: x ** power, row)) for row in matrix]
