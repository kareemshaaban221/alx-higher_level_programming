#!/usr/bin/python3
from sys import argv
l = len(argv) - 1
if l <= 0:
    print("0 arguments.")
    exit
elif l == 1:
    print("1 argument:")
else:
    print("{:d} arguments:".format(l))
i = 0
for val in argv:
    if i != 0:
        print("{:d}: {:s}".format(i, val))
    i += 1
