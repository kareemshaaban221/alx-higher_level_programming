#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    errorMessage = "first_name must be a string"
    errorMessage2 = "last_name must be a string"
    if type(first_name) != str:
        raise TypeError(errorMessage)
    if type(last_name) != str:
        raise TypeError(errorMessage2)
    print("My name is {} {}".format(first_name, last_name), end="")
