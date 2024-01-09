#!/usr/bin/python3
"""Module 0-read_file.
Reads from a file and prints.
"""
import json


def load_from_json_file(filename):
    """Reads from filename and prints
    its contents to stdout.

    Args:
        - filename: name of the file
    """

    with open(filename, 'r') as f:
        return json.loads(f.read())
