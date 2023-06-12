#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    c = sentence[0] if length > 0 else "None"
    tup = length, c
    return(tup)
