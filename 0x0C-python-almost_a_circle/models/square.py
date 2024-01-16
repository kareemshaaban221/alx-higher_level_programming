#!/usr/bin/python3
""" My class module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """

    def __init__(self, size, x=0, y=0, id=None):
        """_summary_

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """_summary_
        """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        """_summary_
        """
        return self.width

    @size.setter
    def size(self, val):
        """_summary_

        Args:
            val (_type_): _description_
        """
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """_summary_
        """
        length = len(args)
        if length <= 0:
            if kwargs is not None:
                for k, v in kwargs.items():
                    setattr(self, k, v)
        else:
            self.id = args[0]
            if length > 1:
                self.size = args[1]
            if length > 2:
                self.x = args[2]
            if length > 3:
                self.y = args[3]

    def to_dictionary(self):
        """_summary_
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
