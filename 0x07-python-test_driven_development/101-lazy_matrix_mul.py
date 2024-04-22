#!/usr/bin/python3
"""
Module that performs matrix multiplication by numpy
matrix_mul:
    takes 2 matrices and returns their product
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 Matrices using numpy module
    Returns:
        the product of 2 matrices
    """
    return np.matmul(m_a, m_b)
