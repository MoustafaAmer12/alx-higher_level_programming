#!/usr/bin/python3
"""
Module that performs matrix multiplication
matrix_mul:
    takes 2 matrices and returns their product
"""


def matrix_mul(m_a, m_b):
    """
    Returns:
        the product of 2 matrices
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for i in range(len(m_a)):
        if type(m_a[i]) is not list:
            raise TypeError("m_a must be a list of lists")
    for i in range(len(m_b)):
        if type(m_b[i]) is not list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    size = len(m_a[0])
    for i in range(len(m_a)):
        if size != len(m_a[i]):
            raise TypeError("each row of m_a must be of the same size")
        for j in range(len(m_a[0])):
            if type(m_a[i][j]) is not int and\
               type(m_a[i][j]) is not float:
                raise TypeError("m_a should contain only integers or floats")
    size = len(m_b[0])
    for i in range(len(m_b)):
        if size != len(m_b[i]):
            raise TypeError("each row of m_b must be of the same size")
        for j in range(len(m_b[0])):
            if type(m_b[i][j]) is not int and\
               type(m_b[i][j]) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    mult = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                mult[i][j] += m_a[i][k] * m_b[k][j]
    return mult
