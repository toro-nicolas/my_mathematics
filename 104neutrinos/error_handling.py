#!/bin/python3
from sys import (argv)
from get_mean import *


#CE SONT NOS COMMENTAIRES PAS CHATGPT MERCI


def usage():
    if len(argv) == 2:
        if argv[1] == "-h":
            print("USAGE\n    ./104neutrinos n a h sd"
                  "\n\nDESCRIPTION\n    n       number of values"
                  "\n    a       arithmetic mean"
                  "\n    h       harmonic mean"
                  "\n    sd      standard deviation")
            exit(0)
        else:
            print("Invalid argument")
            exit(84)
    return 0


def error_handling():
    if len(argv) != 5:
        print("Enter only 4 arguments please")
        exit(84)
    try:
        n = int(argv[1])
        a = float(argv[2])
        h = float(argv[3])
        sd = float(argv[4])
    except:
        print("Please, enter only valid arguments")
        exit(84)
    if sd < 0:
        # la standard deviation = cette formule : sqrt((1/n) * sum((x - a) ** 2))
        # donc elle ne peut pas être négative car on fait la racine carrée d'un nombre
        # est supérieur à 0
        print("standard deviation must be greater than 0")
        exit(84)
    return 0


def error_handling_values(value):
    try:
        value = int(value)
    except:
        print("Please, a value not a string")
        exit(84)
    if value == 0:
        print("Value can't be 0")
        exit(84)
    return value


def error_nb(n):
    if n < 1:
        print("n must be greater than 0")
        exit(84)
    return n


def check_means(count, a, h, sd, value, root):
    try:
        a = get_arithmetic_mean(count, a, value)
    except:
        print("Problem in arithmetic...")
        exit(84)
    try:
        root = get_root_mean_square(root, value, count)
    except:
        print("Problem in root...")
        exit(84)
    try:
        h = get_harmonic_mean(count, h, value)
    except:
        print("Problem in harmonic...")
        exit(84)
    try:
        sd = get_standard_deviation(a, root)
    except:
        print("Problem in standard deviation...")
        exit(84)
    return a, sd, root, h

