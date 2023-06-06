#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = number % 10
print("Last digit of {} is {} and is ".format(number, number2), end='')
if number2 > 5:
    print("greater than 5")
elif number2 == 0:
    print("0")
else:
    print("less than 6 and not 0")
