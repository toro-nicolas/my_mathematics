#!/bin/python3
from matrix import *


def get_matrix_size(argv):
    if len(argv[2]) == 1:
        return 1
    elif len(argv[2]) < 5:
        return 2
    elif len(argv[2]) < 10:
        return 3
    else:
        return 4


def get_str_matrix(argv):
    str_matrix = [[]]
    size = get_matrix_size(argv)
    row = 0
    for i in range(len(argv[1])):
        str_matrix[row].append(ord(argv[1][i]))
        if (i + 1) != len(argv[1]) and (i + 1) % size == 0:
            str_matrix.append([])
            row += 1
    while len(str_matrix[row]) < size:
        str_matrix[row].append(0)
    return str_matrix


def get_message_matrix(argv):
    message_matrix = [[]]
    size = get_matrix_size(argv)
    numbers_list = list(argv[1].split(" "))
    row = 0
    for i in range(len(numbers_list)):
        message_matrix[row].append(int(numbers_list[i]))
        if (i + 1) != len(argv[1]) and (i + 1) % size == 0:
            message_matrix.append([])
            row += 1
    while len(message_matrix[row]) < size:
        message_matrix[row].append(0)
    return message_matrix


def encrypt_message(argv, key_matrix):
    print("Encrypted message:")
    str_matrix = get_str_matrix(argv)
    str_matrix = matrix_product(str_matrix, key_matrix)
    for i in range(len(str_matrix)):
        for j in range(len(str_matrix[i])):
            if j == len(str_matrix[i]) - 1 and i == len(str_matrix) - 1:
                print(str_matrix[i][j])
            else:
                print(str_matrix[i][j], end=" ")


def decrypt_message(argv, key_matrix):
    print("Decrypted message:")
    message_matrix = get_message_matrix(argv)
    message_matrix = matrix_product(message_matrix, key_matrix)
    for i in range(len(message_matrix)):
        for j in range(len(message_matrix[i])):
            try:
                if 32 <= int(round(message_matrix[i][j], 0)) <= 126:
                    print(chr(int(round(message_matrix[i][j], 0))), end="")
            except:
                print("\nInvalid key")
                exit(84)
    print()
