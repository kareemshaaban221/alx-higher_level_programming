#!/usr/bin/python3
""" My class module
"""


def pascal_triangle(n):
    """_summary_

    Args:
        n (_type_): _description_
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    res = [[1], [1, 1]]
    pre = [1, 1]
    for i in range(2, n):
        to_append = [1]
        for j in range(len(pre) - 1):
            to_append.append(pre[j] + pre[j + 1])
        to_append.append(1)
        res.append(to_append)
        pre = to_append
    return res
