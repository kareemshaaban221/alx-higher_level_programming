#!/usr/bin/python3
"""
This Module is for define Square Class
"""


class Square:
    """
    Square Class
    """

    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            # * shifting in y axis
            for b in range(self.position[1]):
                print()
            for i in range(self.__size):
                # * shifting in x axis
                for a in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
