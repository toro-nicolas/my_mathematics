from sys import stderr


def check_args(argv, volume, ph):
    if len(argv) != 2:
        print("Invalid number of arguments", file=stderr)
        return 84
    try:
        with open(argv[1], 'r') as file:
            for line in file:
                line = line.strip().split(';')
                if len(line) != 2 or float(line[0]) < 0 or float(line[1]) < 0:
                    print("Invalid file format", file=stderr)
                    return 84
                volume.append(float(line[0]))
                ph.append(float(line[1]))
    except FileNotFoundError:
        print("Invalid file", file=stderr)
        return 84
    except ValueError:
        print("Invalid file format", file=stderr)
        return 84
    return 0
