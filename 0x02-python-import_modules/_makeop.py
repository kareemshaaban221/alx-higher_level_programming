from calculator_1 import add, sub, mul, div

def makeOp(x, y, op):
    if op == 0:
        return add(x, y)
    elif op == 1:
        return sub(x, y)
    elif op == 2:
        return mul(x, y)
    else:
        return div(x, y)