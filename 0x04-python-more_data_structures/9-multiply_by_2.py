#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = {}
    for k in a_dictionary:
        res[k] = a_dictionary[k] * 2
    return res
