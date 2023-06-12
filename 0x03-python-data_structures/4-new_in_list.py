#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    res = None
    if my_list is None:
        return res
    res = []
    i = 0
    while i < len(my_list):
        if i != idx:
            res.append(my_list[i])
        else:
            res.append(element)
        i += 1
    return res
