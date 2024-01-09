#!/usr/bin/python3
"""Module 0-read_file.
Reads from a file and prints.
"""


def append_write(filename="", text=""):
    """Reads from filename and prints
    its contents to stdout.

    Args:
        - filename: name of the file
    """

    with open(filename, 'a') as f:
        return f.write(text)
