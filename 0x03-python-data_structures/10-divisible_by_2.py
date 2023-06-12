#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ml = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            ml[count] = True
        else:
            ml[count] = False
    return ml
