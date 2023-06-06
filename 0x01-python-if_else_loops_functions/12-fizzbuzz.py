#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        fizz = ((i % 3) == 0)
        buzz = ((i % 5) == 0)
        if fizz and buzz:
            print("FizzBuzz ", end='')
        elif fizz:
            print("Fizz ", end='')
        elif buzz:
            print("Buzz ", end='')
        else:
            print("{:d} ".format(i), end='')
