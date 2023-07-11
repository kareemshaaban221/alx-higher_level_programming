#!/usr/bin/python3
"""
Module text_indentation
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:.,? and :
    :param text:
    :return:
    """
    if type(text) != str:
        raise TypeError('text must be a string')
    for char in text:
        print(char, end='')
        if char == '.' or char == '?' or char == ':':
            print('\n')
