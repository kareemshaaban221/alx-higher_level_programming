#!/usr/bin/python3
from sys import argv
length = len(argv) - 1
if length <= 0:
    print("0 arguments.")
    exit
elif length == 1:
    print("1 argument:")
else:
    print("{:d} arguments:".format(length))
i = 0
for val in argv:
    if i != 0:
        print("{:d}: {:s}".format(i, val))
    i += 1
