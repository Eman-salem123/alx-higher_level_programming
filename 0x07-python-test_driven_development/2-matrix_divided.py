#!/usr/bin/python3
""" matrix divided module"""


def matrix_divided(matrix, div):
    """ divide numbers in list of list"""
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(raw) == len(matrix[0]) for raw in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrixnew = [list(map(lambda a: round(a/div, 2), num)) for num in matrix]
    return matrixnew
