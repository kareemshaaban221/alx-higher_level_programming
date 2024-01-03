#!/usr/bin/python3
"""
Module print square
Prints a given first name and last name.
"""


def print_square(size):
    """
    Prints a square of given size.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
