#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for i in range(len(matrix[row])):
            if i != len(matrix[row]) - 1:
                print("{:d}".format(matrix[row][i]), end=" ")
            else:
                print("{:d}".format(matrix[row][i]), end="")
        if row != len(matrix) - 1:
            print()
    print()
