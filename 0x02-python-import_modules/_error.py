from sys import stderr

def err(type):
    if type == 0:
        stderr.write('Usage: ./100-my_calculator.py <a> <operator> <b>\n')
        exit(1)
    else:
        stderr.write('Unknown operator. Available operators: +, -, * and /\n')
        exit(1)