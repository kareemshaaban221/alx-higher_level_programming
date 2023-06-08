#!/usr/bin/python3
from sys import argv
l = len(argv) - 1
if l <= 0:
    print("0 arguments.")
    exit
elif l < 2:
    print("{:d} argument:".format(l))
else:
    print("{:d} arguments:".format(l))
i = 0
for val in argv:
    if i != 0:
        print("{:d}: {:s}".format(i, val))
    i += 1
