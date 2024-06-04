from sys import stderr
from math import sqrt

def check_args(argv):
    if len(argv) < 3:
        print("Invalid number of arguments", file=stderr)
        return 84
    for j in range(2, len(argv)):
        try:
            float(argv[j])
        except ValueError:
            print("Invalid argument", file=stderr)
            return 84
    if (sqrt(len(argv) - 2)) % 1 != 0:
        print("Matrix has to be square", file=stderr)
        return 84
    return 0
