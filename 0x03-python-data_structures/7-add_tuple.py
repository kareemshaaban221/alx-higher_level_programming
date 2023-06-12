#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta = tuple_a
    tb = tuple_b
    a, b = 0, 0
    if len(ta) >= 1:
        a += ta[0]
    if len(tb) >= 1:
        a += tb[0]
    if len(ta) >= 2:
        b += ta[1]
    if len(tb) >= 2:
        b += tb[1]
    return (a, b)
