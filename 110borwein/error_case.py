from sys import stderr


def check_args(argv, n):
    if len(argv) != 2:
        print("Invalid number of arguments", file=stderr)
        return 84
    try:
        if int(argv[1]) < 0:
            print("Invalid number", file=stderr)
            return 84
        n.append(int(argv[1]))
    except:
        print("An error occured", file=stderr)
        return 84
    return 0
