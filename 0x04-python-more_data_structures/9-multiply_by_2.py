#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = {}
    for k, v in a_dictionary:
        if v % 2 == 0:
            res[k] = v
    return res

print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
