#!/usr/bin/python3
def element_at(my_list, idx):
    ll = len(my_list)
    if idx < 0 or idx >= ll:
        return None
    else:
        return my_list[idx]
