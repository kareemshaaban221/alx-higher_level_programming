#!/usr/bin/env python3
def no_c(my_string):
    if my_string is None:
        return None
    res = ''
    for c in my_string:
        if c == 'c' or c == 'C':
            continue
        res += c
    return res
