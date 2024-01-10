#!/usr/bin/python3
""" My class module
"""


class Student:
    """ My class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        di = self.__dict__
        res = {}
        if type(attrs) is list:
            for k, v in di.items():
                if k in attrs:
                    res[k] = v
        else:
            return di
        return res

    def reload_from_json(self, json):
        self.__dict__.clear()
        print(self.first_name)
        for k, v in json.items():
            self.__dict__[k] = v
