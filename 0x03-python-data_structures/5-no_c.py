#!/usr/bin/env python3
def no_c(my_string):
    res = ''
    for c in my_string:
        if c is not 'c' and c is not 'C':
            continue
        res += c
    return res
