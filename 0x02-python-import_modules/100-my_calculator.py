#!/usr/bin/python3
from sys import argv
from _makeop import makeOp
from _error import err

if __name__ == '__main__':
    length = len(argv) - 1

    if (length != 3):
        err(0)

    x = int(argv[1])
    y = int(argv[3])
    op = argv[2]
    res = None
    if op == '+':
        res = makeOp(x, y, 0)
    elif op == '-':
        res = makeOp(x, y, 1)
    elif op == '*':
        res = makeOp(x, y, 2)
    elif op == '/':
        res = makeOp(x, y, 3)
    else:
        err(1)

    print("{:d} {:s} {:d} = {:d}".format(x, op, y, res))
