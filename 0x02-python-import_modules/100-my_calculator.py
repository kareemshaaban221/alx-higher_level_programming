#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
from sys import stderr

def makeOp(x, y, op):
    if op == 0:
        return add(x, y)
    elif op == 1:
        return sub(x, y)
    elif op == 2:
        return mul(x, y)
    else:
        return div(x, y)
    
def err(type):
    if type == 0:
        stderr.write('Usage: ./100-my_calculator.py <a> <operator> <b>\n')
        exit(1)
    else:
        stderr.write('Unknown operator. Available operators: +, -, * and /\n')
        exit(1)

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
