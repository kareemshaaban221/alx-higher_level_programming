#!/usr/bin/python3
"""
===========================
Module with class MyList
===========================
"""


class BaseGeometry():
    """_summary_

    Args:
        list (_type_): _description_
    """
    def area(self):
        """_summary_
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """_summary_

        Args:
            name (_type_): _description_
            value (_type_): _description_
        """
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
