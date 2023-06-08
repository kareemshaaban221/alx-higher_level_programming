#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    i = 0
    res = 0
    for val in argv:
        if i != 0:
            res += int(val)
        i += 1
    print("{}".format(res))
