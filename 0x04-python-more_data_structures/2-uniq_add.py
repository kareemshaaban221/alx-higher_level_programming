#!/usr/bin/python3
def uniq_add(my_list=[]):
    added = []
    res = 0
    for i in my_list:
        if i not in added:
            res += i
            added.append(i)
    return res
