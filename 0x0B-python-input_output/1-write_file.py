#!/usr/bin/python3
"""Module 0-read_file.
Reads from a file and prints.
"""


def write_file(filename="", text=""):
    """Reads from filename and prints
    its contents to stdout.

    Args:
        - filename: name of the file
    """

    with open(filename, 'w') as f:
        return f.write(text)
