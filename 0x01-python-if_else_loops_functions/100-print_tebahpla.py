#!/usr/bin/python3
upper = False
res = ''
for i in range(122, 96, -1):
    if upper:
        i -= 32
        upper = False
    else:
        upper = True
    res += chr(i)
print("{:s}".format(res), end='')
