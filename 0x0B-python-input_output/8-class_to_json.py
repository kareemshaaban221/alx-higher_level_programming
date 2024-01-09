#!/usr/bin/python3
"""Module 0-read_file.
Reads from a file and prints.
"""
import json


def class_to_json(obj):
    """_summary_

    Args:
        obj (_type_): _description_
    """
    return json.dumps(obj.__dict__)
