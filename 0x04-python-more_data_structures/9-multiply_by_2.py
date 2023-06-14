#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = {}
    for k, v in a_dictionary:
        if v % 2 == 0:
            res[k] = v
    return res
