__author__ = 'ubuntu'

import random

size = 10 # size of builded square matrixes

def make(size):
    first = [[random.randint(1,100) for x in range(size)] for x in range(size)]
    second = [[random.randint(1,100) for x in range(size)] for x in range(size)]

    with open('first.txt','w') as first_file:
        for line in first:
            first_file.write(str(line) + '\n')

    with open('second.txt','w') as second_file:
        for line in second:
            second_file.write(str(line) + '\n')

if __name__ == '__main__':
    make(size)
