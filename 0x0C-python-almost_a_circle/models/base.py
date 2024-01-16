#!/usr/bin/python3
""" My class module
"""
import json


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

    def to_dictionary(self):
        """_summary_
        """
        return {
            'id': self.id,
        }

    @staticmethod
    def to_json_string(list_dictionaries):
        """_summary_

        Args:
            list_dictionaries (_type_): _description_
        """
        is_none = list_dictionaries is None
        not_list = type(list_dictionaries) is not list
        if is_none or not_list or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """_summary_

        Args:
            list_objs (_type_): _description_
        """
        for i in range(len(list_objs)):
            list_objs[i] = list_objs[i].to_dictionary()
        content = cls.to_json_string(list_objs)
        with open(cls.__name__+".json", "w") as f:
            f.write(content)

    @staticmethod
    def from_json_string(json_string):
        """_summary_

        Args:
            json_string (_type_): _description_
        """
        is_none = json_string is None
        not_list = type(json_string) is not str
        if is_none or not_list or json_string == '':
            return []
        return json.loads(json_string)

    def setCounter(val):
        """_summary_

        Args:
            val (_type_): _description_
        """
        Base.__nb_objects = val
