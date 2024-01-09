#!/usr/bin/python3
"""
===========================
Module with class MyList
===========================
"""


def add_attribute(obj, name, value):
    """_summary_

    Args:
        obj (_type_): _description_
        name (_type_): _description_
        value (_type_): _description_
    """

    if isinstance(obj, dict):
        obj.__setattr__(name, value)
    else:
        raise TypeError("can't add new attribute")
