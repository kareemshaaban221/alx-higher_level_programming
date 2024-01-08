#!/usr/bin/python3
"""
This is new module
"""


class MyList(list):
    """
    MyList class
    """
    def print_sorted(self):
        """
        function to sort
        """
        print(sorted(list(self)))
