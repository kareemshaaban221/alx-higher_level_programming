#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    res = ''
    for c in str:
        if i != n:
            res += c
        i += 1
    return res
