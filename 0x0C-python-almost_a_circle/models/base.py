#!/usr/bin/python3
""" My class module
"""
import json
import csv


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
        list_objs_dict = []
        for i in range(len(list_objs)):
            list_objs_dict.append(list_objs[i].to_dictionary())
        content = cls.to_json_string(list_objs_dict)
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

    @classmethod
    def create(cls, **dictionary):
        """_summary_
        """
        obj = cls.dummy_instance()
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        content = ""
        with open(cls.__name__+".json", "r") as f:
            content = f.read()
        if content == "":
            return []
        dicts = cls.from_json_string(content)
        return [cls.create(**dict) for dict in dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """_summary_

        Args:
            list_objs (_type_): _description_

        Returns:
            _type_: _description_
        """
        list_objs_dict = []
        for i in range(len(list_objs)):
            list_objs_dict.append(list_objs[i].to_dictionary())
        with open(cls.__name__+".csv", "w") as f:
            writer = csv.DictWriter(f, cls.getCols(), lineterminator='\n')
            writer.writerows(list_objs_dict)

    @classmethod
    def load_from_file_csv(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        objs = []
        with open(cls.__name__+".csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader.reader:
                for i in range(len(row)):
                    row[i] = int(row[i])
                obj = dict(zip(cls.getCols(), row))
                objs.append(cls.create(**obj))
        return objs

    @staticmethod
    def dummy_instance():
        """_summary_
        """
        return Base()

    @staticmethod
    def getCols():
        """_summary_
        """
        return ['id']

    def setCounter(val):
        """_summary_

        Args:
            val (_type_): _description_
        """
        Base.__nb_objects = val
