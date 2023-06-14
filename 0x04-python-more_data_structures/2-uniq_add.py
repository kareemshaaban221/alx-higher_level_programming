#!/usr/bin/python3
def uniq_add(my_list=[]):
    lis = set(my_list)
    res = 0
    for i in lis:
        res += i
    return res
