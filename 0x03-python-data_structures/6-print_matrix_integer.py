#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    height = len(matrix)
    for i in range(height):
        width = len(matrix[i])
        for j in range(width):
            print("{:d}".format(matrix[i][j]), end=" " if j + 1 != width else "")
        print("")
