#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for i in matrix:
        temp = []
        for j in i:
            temp.append(j * j)
        res.append(temp)
    return res
