from sys import stderr


def check_args(args):
    try:
        num = []
        den = []
        for index in range(1, len(args), 2):
            num.append([int(elt) for elt in args[index].split("*")])
            den.append([int(elt) for elt in args[index + 1].split("*")])
    except:
        print("Bad arguments values", file=stderr)
        exit(84)
    return num, den
