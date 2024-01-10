#!/usr/bin/python3
""" My class module
"""
from sys import stdin


def print_stats(lines):
    """sumary_line"""
    statuscodes = {'200': 0, '301': 0, '400': 0, '401': 0,
                   '403': 0, '404': 0, '405': 0, '500': 0}
    total_file_size = 0
    for line in lines:
        arr = str(line).split()
        statuscode = arr[len(arr) - 2]
        statuscodes[statuscode] += 1
        filesize = arr[len(arr) - 1]
        total_file_size += int(filesize)
    print(f"File size: {total_file_size}")
    for k, v in statuscodes.items():
        if statuscodes[k] > 0:
            print(f"{k}: {v}")

lines = []
i = 0
while True:
    try:
        lines.append(stdin.readline())
    except KeyboardInterrupt as e:
        print_stats(lines)
        break;
    i += 1
    if i % 10 == 0:
        i = 0
        print_stats(lines)
        lines = []
raise KeyboardInterrupt
