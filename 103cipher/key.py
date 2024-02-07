#!/bin/python3
from matrix import *


def print_key_matrix(key_matrix):
    print("Key matrix:")
    for i in range(len(key_matrix)):
        for j in range(len(key_matrix)):
            if (j + 1) % len(key_matrix) == 0:
                print(round(key_matrix[i][j], 3))
            else:
                print(round(key_matrix[i][j], 3), end="\t")
    print()


def fill_key_matrix(argv, key_matrix, size):
    for i in range(size):
        key_matrix.append([])
        for j in range(size):
            try:
                key_matrix[i].append(ord(argv[2][i * size + j]))
            except:
                key_matrix[i].append(0)


def get_key_matrix(argv):
    key_matrix = []
    if len(argv[2]) == 1:
        key_matrix.append([])
        key_matrix[0].append(ord(argv[2][0]))
    elif len(argv[2]) < 5:
        fill_key_matrix(argv, key_matrix, 2)
    elif len(argv[2]) < 10:
        fill_key_matrix(argv, key_matrix, 3)
    else:
        fill_key_matrix(argv, key_matrix, 4)
    return key_matrix


def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for nb in range(len(matrix)):
        det = det + ((-1)**nb) * matrix[0][nb] * determinant(minor(matrix, 0, nb))
    return det


def minor(matrix, i, j):
    minor_matrix = []
    for row in (matrix[:i] + matrix[i+1:]):
        minor_matrix.append(row[:j] + row[j+1:])
    return minor_matrix


def cofactor_matrix(matrix):
    cofactors_matrix = []
    for r in range(len(matrix)):
        cofactor_row = []
        for c in range(len(matrix)):
            minor_det = determinant(minor(matrix, r, c))
            cofactor_row.append(((-1)**(r+c)) * minor_det)
        cofactors_matrix.append(cofactor_row)
    return cofactors_matrix


def change_matrix_sens(matrix):
    transposed_matrix = []
    for row in range(len(matrix)):
        transposed_matrix.append([])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j].append(matrix[i][j])
    return transposed_matrix


def inverse_matrix(matrix):
    if len(matrix) == 1:
        new_matrix = [[1 / matrix[0][0]]]
        return new_matrix
    if len(matrix) == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        if det == 0:
            print("Invalid key")
            exit(84)
        new_matrix = [[0, 0], [0, 0]]
        new_matrix[0][0] = matrix[1][1] / det
        new_matrix[0][1] = -matrix[0][1] / det
        new_matrix[1][0] = -matrix[1][0] / det
        new_matrix[1][1] = matrix[0][0] / det
        return new_matrix
    det = determinant(matrix)
    if det == 0:
        print("Invalid determinant")
        exit(84)
    cofactors = cofactor_matrix(matrix)
    cofactors = change_matrix_sens(cofactors)
    matrix = []
    for row in range(len(cofactors)):
        matrix.append([])
        for col in range(len(cofactors[row])):
            matrix[row].append(cofactors[row][col] / det)
    return matrix


def round_zero(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == -0.0:
                matrix[row][col] = 0.0
