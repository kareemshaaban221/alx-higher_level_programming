#!/usr/bin/python3
""" My class module
"""


class Base():
    """ My class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """_summary_

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def setCounter(val):
        """_summary_

        Args:
            val (_type_): _description_
        """
        Base.__nb_objects = val
