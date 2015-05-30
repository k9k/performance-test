__author__ = 'ubuntu'

import ast
import numpy
from make_matrixes import size


first = [[0 for x in range(size)] for x in range(size)]
second = [[0 for x in range(size)] for x in range(size)]

class DifferentSizeMatriXError(Exception):
    pass

class NotMatrixError(Exception):
    pass


def load_matrixes():
    with open('first.txt', 'r') as first_file:
        for index, line in enumerate(first_file):
            first[index] = ast.literal_eval(line)

    with open('second.txt', 'r') as second_file:
        for index, line in enumerate(second_file):
            second[index] = ast.literal_eval(line)
    return first, second

def multiply(first, second):
    try:
        if len(first[0]) != len(second):
            raise DifferentSizeMatriXError
        result = numpy.matrix(first) * numpy.matrix(second)
        return numpy.matrix(result).tolist()     # change numpy.matrix to a list
    except TypeError:
        raise NotMatrixError
        print('only matrixes allowed')

def main():
    first_matrix, second_matrix = load_matrixes()
    multiply(first_matrix, second_matrix)