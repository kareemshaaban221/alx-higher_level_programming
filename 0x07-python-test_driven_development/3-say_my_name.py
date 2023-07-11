#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if type(first_name) != str and type(last_name) != str:
        raise TypeError("first_name must be a string or last_name must be a string")
    print("My name is {} {}".format(first_name, last_name), end="")
