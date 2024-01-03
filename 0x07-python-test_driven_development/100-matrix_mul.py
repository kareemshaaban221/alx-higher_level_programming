#!/usr/bin/python3
"""
Module 100-matix_mul
"""


def verify_list_type(var, mat_name):
    """
    function verify_list_type
    """
    if type(var) is not list:
        raise TypeError(f'{mat_name} must be a list')


def verify_list_elements_type(mat, mat_name):
    """
    function verify_list_elements_type
    """
    msg1 = f'{mat_name} must be a list of lists'
    msg2 = f'{mat_name} should contain only integers or floats'
    for i in mat:
        if type(i) is not list:
            raise TypeError(msg1)
        else:
            for j in i:
                if type(j) not in [int, float]:
                    raise TypeError(msg2)


def verify_mat_len(mat, mat_name):
    """
    function verify_mat_len
    """
    if len(mat) == 0 or (len(mat[0]) == 0 and len(mat) == 1):
        raise ValueError(f'{mat_name} can\'t be empty')


def verify_mat_rec(mat, mat_name):
    """
    function verify_mat_rec
    """
    length = len(mat[0])
    for i in mat:
        if len(i) != length:
            raise TypeError(f'each row of {mat_name} must be of the same size')


def verify_mat_mul(ma, mb):
    """
    function verify_mat_mul
    """
    if len(ma[0]) != len(mb):
        raise ValueError('m_a and m_b can\'t be multiplied')


def res_mat_dims(ma, mb):
    """
    function res_mat_dims
    """
    return (len(ma), len(mb[0]))


def mul_row_col(ma, mb, row, col):
    """
    function mul_row_col
    """
    row = ma[row]
    col = [i[col] for i in mb]
    res = 0
    for i in range(len(row)):
        res += (row[i] * col[i])
    return res


def matrix_mul(m_a, m_b):
    """
    funtion matrix_mul
    """
    verify_list_type(m_a, 'm_a')
    verify_list_type(m_b, 'm_b')
    verify_list_elements_type(m_a, 'm_a')
    verify_list_elements_type(m_b, 'm_b')
    verify_mat_len(m_a, 'm_a')
    verify_mat_len(m_b, 'm_b')
    verify_mat_rec(m_a, 'm_a')
    verify_mat_rec(m_b, 'm_b')
    verify_mat_mul(m_a, m_b)
    dims = res_mat_dims(m_a, m_b)
    res = []
    for i in range(dims[0]):
        res_temp = []
        for j in range(dims[1]):
            res_temp.append(mul_row_col(m_a, m_b, i, j))
        res.append(res_temp)
    return res
