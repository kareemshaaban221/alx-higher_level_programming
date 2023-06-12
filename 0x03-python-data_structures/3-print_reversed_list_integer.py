#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    res = []
    i = len(my_list) - 1
    while i >= 0:
        res.append(my_list[i])
        i -= 1
    return res

