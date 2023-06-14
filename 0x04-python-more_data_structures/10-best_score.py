#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    res = None
    for k in a_dictionary:
        if res is None:
            res = k
            continue
        else:
            if a_dictionary[res] < a_dictionary[k]:
                res = k
    return res
