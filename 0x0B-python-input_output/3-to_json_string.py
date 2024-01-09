#!/usr/bin/python3
import json
"""Module 0-read_file.
Reads from a file and prints.
"""


def to_json_string(my_obj):
    """Reads from filename and prints
    its contents to stdout.

    Args:
        - filename: name of the file
    """

    try:
        return json.dumps(my_obj)
    except TypeError as e:
        raise TypeError(f"{my_obj} is not JSON serializable")
