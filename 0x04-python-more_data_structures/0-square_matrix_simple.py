#!/usr/bin/python3

def square_matrix_simple(matrix=None):
    if matrix is None:
        return None

    new_matrix = []
    for i in matrix:
        new_row = []
        for j in i:
            new_row.append(j * j)
        new_matrix.append(new_row)

    return new_matrix
