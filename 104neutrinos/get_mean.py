#!/bin/python3
from math import (sqrt)


def get_first_standard_deviation(count, sd, value, a):
    return sqrt(count / (count + 1) * (sd ** 2) + ((value - a) ** 2) / (count + 1))


def get_standard_deviation(a, root):
    return sqrt((root ** 2) - (a ** 2))


def get_root_mean_square(root, value, count):
    sum_of_squares = count * (root ** 2)
    sum_of_squares += value ** 2
    updated_rms = (sum_of_squares / (count + 1)) ** 0.5
    return updated_rms

def get_root_mean_square_first(sd, a):
    return sqrt((a ** 2) + (sd ** 2))


def get_harmonic_mean(count, h, value):
    # initial_sum = Un
    # final_sum = Un+1
    initial_sum = count / h
    final_sum = initial_sum + (1 / value)
    return (count + 1) / final_sum


def get_factor_commun(v1, div1, v2, div2):
    return (v1 * div2 + v2 * div1) / (div1 * div2)


def get_arithmetic_mean(count, a, value):
    # a est tout simplement une moyenne arithmétique.
    # on fait la somme de toutes les valeurs et on divise par le nombre de valeurs
    a = ((a * count) + value) / (count + 1)
    return a
