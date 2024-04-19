#!/usr/bin/python3
"""
"""


def matrix_divided(matrix, div):
    if type(matrix) is not list or type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(size):
            if type(matrix[i][j]) is not int and type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(matrix[i][j] / div, 2) for j in range(size)] for i in range(len(matrix))]
    return new_matrix
