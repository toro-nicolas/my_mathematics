#!/bin/python3


def matrix_product(matrix_1, matrix_2):
    result = []
    for row in range(len(matrix_1)):
        result.append([])
        for col in range(len(matrix_1[row])):
            result[row].append(0)
            for k in range(len(matrix_1[row])):
                result[row][col] += matrix_1[row][k] * matrix_2[k][col]
    return result


def multiply_row(matrix, row, factor):
    for i in range(len(matrix)):
        matrix[row][i] *= factor


def divide_row(matrix, row, factor):
    for i in range(len(matrix)):
        matrix[row][i] /= factor


def substract_row(matrix, row1, row2):
    for i in range(len(matrix)):
        matrix[row1][i] -= matrix[row2][i]


def copy_matrix(matrix):
    result = []
    for i in range(len(matrix)):
        result.append([])
        for j in range(len(matrix)):
            result[i].append(matrix[i][j])
    return result


def get_identy_matrix(size):
    matrix = []
    for i in range(size):
        matrix.append([])
        for j in range(size):
            if i == j:
                matrix[i].append(1)
            else:
                matrix[i].append(0)
    return matrix
