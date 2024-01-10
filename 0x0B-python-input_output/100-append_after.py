#!/usr/bin/python3
""" My class module
"""


def append_after(filename="", search_string="", new_string=""):
    """_summary_

    Args:
        n (_type_): _description_
    """
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    new_content = ""
    for line in lines:
        new_content += line
        if search_string in line:
            new_content += new_string
    with open(filename, 'w') as f:
        f.write(new_content)
