#!/usr/bin/python3
""" My class module
"""
from sys import stdin


dictstatus = {}
totalsize = 0
totalcount = 0
for line in stdin:
    split = line.split()
    status = split[-2]
    totalsize += int(split[-1])
    if status in dictstatus.keys():
        dictstatus[status] += 1
    else:
        dictstatus[status] = 1
    totalcount += 1
    if totalcount == 10:
        sortme = sorted(dictstatus.keys())
        print(f"File size: {totalsize}")
        for keys in sortme:
            print("{}: {}".format(keys, dictstatus[keys]))
        totalcount = 0
        totalsize = 0
        dictstatus = {}
        continue
