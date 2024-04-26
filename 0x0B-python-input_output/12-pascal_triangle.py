#!/usr/bin/python3
"""
A Module that defines a function to create
the pascal triangle of size n.
"""


def pascal_triangle(n):
    """A Function that creates the pascal
    triangle of a given height.
    Returns:
        A list of lists representing the pascal
        triangle
    """
    triangle = [[0 for i in range(j + 1)] for j in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                triangle[i][j] = 1
            else:
                triangle[i][j] = triangle[i-1][j-1] +\
                                 triangle[i-1][j]
    return triangle
