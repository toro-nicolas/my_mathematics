
from sys import argv, stderr


def check_two_args():
    try:
        n = int(argv[1])
        k = float(argv[2])
        if k >= 1 and k <= 4 and n >= 0:
            pass
        else:
            print("k must be between 1 and 4 and n must be positive", file=stderr)
            exit(84)
    except:
        exit(84)
    return n, k


def check_three_args():
    try:
        n = int(argv[1])
        i0 = int(argv[2])
        i1 = int(argv[3])
        if n >= 0 and i0 >= 1 and i0 <= i1:
            pass
        else:
            print("n, i0 and i1 must be positive and i0 < i1", file=stderr)
            exit(84)
    except:
        exit(84)
    return n, i0, i1
