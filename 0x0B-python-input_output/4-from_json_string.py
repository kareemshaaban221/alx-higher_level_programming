#!/usr/bin/python3
"""Module 0-read_file.
Reads from a file and prints.
"""
import json


def from_json_string(my_str):
    """Reads from filename and prints
    its contents to stdout.

    Args:
        - filename: name of the file
    """

    return json.loads(my_str)
