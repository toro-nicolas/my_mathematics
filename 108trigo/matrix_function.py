import math


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                print("{:.2f}".format(matrix[i][j]))
            else:
                print("{:.2f}".format(matrix[i][j]), end=" ")
    return


def sum_matrix(matrix1, matrix2):
    final_matrix = [[0.00 for i in range(len(matrix1))] for j in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            final_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return final_matrix


def matrix_product(matrix1, matrix2):
    final_matrix = [[0.00 for i in range(len(matrix1))] for j in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            for k in range(len(matrix1)):
                final_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return final_matrix


def matrix_identitaire(matrix):
    n = len(matrix)
    matrice_identitaire = [[0.00 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrice_identitaire[i][j] = 1.00
    return matrice_identitaire


def scalar_multiply(matrix, scalar):
    result = [[0.0 for _ in range(len(matrix))] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] * scalar

    return result


def exp(matrix):
    exp_matrix = matrix_identitaire(matrix)
    temp_matrix = matrix_identitaire(matrix)

    for k in range(1, 50):
        temp_matrix = matrix_product(temp_matrix, matrix)
        exp_matrix = sum_matrix(exp_matrix, scalar_multiply(temp_matrix, 1 / math.factorial(k)))

    return exp_matrix


def matrix_power(matrix, n):
    matrix_a_power_k = matrix
    for i in range(1, n):
        matrix_a_power_k = matrix_product(matrix_a_power_k, matrix)
    return matrix_a_power_k


def cos(matrix):
    cos_matrix = matrix_identitaire(matrix)

    for n in range(1, 50):
        matrix_a_power_k = matrix_power(matrix, 2 * n)
        cos_matrix = sum_matrix(cos_matrix,
            scalar_multiply(matrix_a_power_k, math.pow(-1, n) / math.factorial(2 * n)))
    return cos_matrix


def sin(matrix):
    sin_matrix = matrix

    for n in range(1, 80):
        matrix_a_power_k = matrix_power(matrix, 2 * n + 1)
        sin_matrix = sum_matrix(sin_matrix,
            scalar_multiply(matrix_a_power_k, math.pow(-1, n) / math.factorial(2 * n + 1)))
    return sin_matrix


def cosh(matrix):
    exp_matrix_pos = exp(matrix)
    exp_matrix_neg = exp(scalar_multiply(matrix, -1))

    cosh_matrix = sum_matrix(exp_matrix_pos, exp_matrix_neg)
    cosh_matrix = scalar_multiply(cosh_matrix, 0.5)
    return cosh_matrix


def sinh(matrix):
    exp_matrix_pos = exp(matrix)
    exp_matrix_neg = exp(scalar_multiply(matrix, -1))

    sinh_matrix = sum_matrix(exp_matrix_pos, scalar_multiply(exp_matrix_neg, -1))
    sinh_matrix = scalar_multiply(sinh_matrix, 0.5)
    return sinh_matrix