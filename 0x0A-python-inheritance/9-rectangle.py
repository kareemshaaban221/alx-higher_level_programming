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
        self.__height = height

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__width * self.__height

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"[Rectangle] {self.__width}/<{self.__height}>"

    def __repr__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"[Rectangle] {self.__width}/<{self.__height}>"
