#!/usr/bin/python3
"""Module 0-read_file.
Reads from a file and prints.
"""
import json


def to_json_string(my_obj):
    """Reads from filename and prints
    its contents to stdout.

    Args:
        - filename: name of the file
    """

    return json.dumps(my_obj)
