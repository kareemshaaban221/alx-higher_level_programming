#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) != list or type(matrix[0]) != list or type(matrix[0][0]) not in [int, float]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size = None;
    for i in matrix:
        if size is None:
            size = len(i)
            continue
        else:
            if len(i) != size:
                raise ValueError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("div must not be 0")
    res = []
    for i in matrix:
        temp = []
        for j in i:
            temp.append(round(j / div, 2))
        res.append(temp)