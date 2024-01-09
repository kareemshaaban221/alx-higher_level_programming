#!/usr/bin/python3
"""Module 0-read_file.
Reads from a file and prints.
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
args = sys.argv[1:]
current = []
try:
    current = list(load_from_json_file('add_item.json'))
except Exception as e:
    pass
finally:
    current += list(args)
    save_to_json_file(current, 'add_item.json')
