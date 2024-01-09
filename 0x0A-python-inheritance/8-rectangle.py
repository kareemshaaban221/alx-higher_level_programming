#!/usr/bin/python3
"""
===========================
Module with class MyList
===========================
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """_summary_
    """
    __width = None
    __height = None

    def __init__(self, width, height):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__heigth = height
