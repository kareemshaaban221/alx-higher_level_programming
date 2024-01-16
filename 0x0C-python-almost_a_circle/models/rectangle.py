#!/usr/bin/python3
""" My class module
"""
from models.base import Base


class Rectangle(Base):
    """ My class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__width

    @width.setter
    def width(self, width):
        """_summary_

        Args:
            width (_type_): _description_
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__height

    @height.setter
    def height(self, height):
        """_summary_

        Args:
            height (_type_): _description_
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__x

    @x.setter
    def x(self, x):
        """_summary_

        Args:
            x (_type_): _description_
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__y

    @y.setter
    def y(self, y):
        """_summary_

        Args:
            y (_type_): _description_
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """_summary_
        """
        return self.width * self.height

    def display(self):
        """_summary_
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(end=' ')
            for j in range(self.width):
                print(end='#')
            print()

    def __str__(self):
        """_summary_
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

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
                self.width = args[1]
            if length > 2:
                self.height = args[2]
            if length > 3:
                self.x = args[3]
            if length > 4:
                self.y = args[4]

    def to_dictionary(self):
        """_summary_
        """
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
