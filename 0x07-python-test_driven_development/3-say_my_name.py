#!/usr/bin/python3
"""
Module say_my_name
Prints a given first name and last name.
"""


def say_my_name(first_name, last_name=""):
    """Prints a string with <first_name>
    and <last_name>.
    """
    errorMessage = "first_name must be a string"
    errorMessage2 = "last_name must be a string"
    if type(first_name) != str:
        raise TypeError(errorMessage)
    if type(last_name) != str:
        raise TypeError(errorMessage2)
    print("My name is {} {}".format(first_name, last_name), end="")
