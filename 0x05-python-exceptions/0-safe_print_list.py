#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if x == 0:
        return
    for i in range(x):
        try:
            print(my_list[i], end="")
        except IndexError:
            break
