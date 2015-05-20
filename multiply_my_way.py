__author__ = 'ubuntu'

import ast
from make_matrixes import size

first = [[0 for x in range(size)] for x in range(size)]
second = [[0 for x in range(size)] for x in range(size)]


def load_matrixes():
    with open('first.txt', 'r') as first_file:
        for index, line in enumerate(first_file):
            first[index] = ast.literal_eval(line)

    with open('second.txt', 'r') as second_file:
        for index, line in enumerate(second_file):
            second[index] = ast.literal_eval(line)

    return first, second

def multiply(first, second):
    result = [[0 for x in range(size)] for x in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += first[i][0+k] * second[0+k][j]
    return result


first_matrix, second_matrix = load_matrixes()
multiply(first_matrix, second_matrix)