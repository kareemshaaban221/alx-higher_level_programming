#!/usr/bin/python3
def uppercase(str):
    res = ''
    for i in str:
        if ord(i) >= 65 and ord(i) <= 90:
            res += i
        else:
            res += chr(ord(i) - 32)
    print(res)
