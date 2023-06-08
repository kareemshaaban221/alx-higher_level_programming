#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    res = 0
    for val in argv:
        res += int(val)
    print("{}".format(res))