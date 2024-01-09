#!/usr/bin/python3
"""
===========================
Module with class MyList
===========================
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """_summary_
    """
    __size = None

    def __init__(self, size):
        """_summary_
        """
        Rectangle.__init__(self, size, size)

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"[Square] {self.__width}/{self.__height}"

    def __repr__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"[Square] {self.__width}/{self.__height}"
