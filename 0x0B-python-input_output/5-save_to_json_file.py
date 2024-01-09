#!/usr/bin/python3
"""Module 0-read_file.
Reads from a file and prints.
"""
import json


def save_to_json_file(my_obj, filename):
    """Reads from filename and prints
    its contents to stdout.

    Args:
        - filename: name of the file
    """

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
