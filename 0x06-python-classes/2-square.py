#!/usr/bin/python3
"""
This Module is for define Square Class
"""


class Square:
    """
    Square Class
    """

    __size = None

    def __init__(self, size=0):
        if type(size) != type(int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
