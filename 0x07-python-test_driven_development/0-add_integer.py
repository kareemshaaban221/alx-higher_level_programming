#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Add two integers together
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b