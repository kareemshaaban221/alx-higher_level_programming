#!/usr/bin/python3
def uppercase(str):
    res = ''
    for i in str:
        iNum = ord(i)
        if iNum >= 97 and iNum <= 122:
            res += chr(iNum - 32)
        else:
            res += i
    print(res)
