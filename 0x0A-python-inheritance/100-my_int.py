#!/usr/bin/python3
"""
===========================
Module with class MyList
===========================
"""


class MyInt(int):
    """_summary_
    """

    def __ne__(self, __value: object) -> bool:
        return super().__eq__(__value)

    def __eq__(self, __value: object) -> bool:
        return super().__ne__(__value)
