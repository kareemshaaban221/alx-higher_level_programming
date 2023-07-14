#!/usr/bin/python3

def safe_print_division(a, b):
    res = None
    try:
        res = a/b
    except ZeroDivisionError:
        pass
    finally:
        if res is not None:
            print("{}".format(res))
