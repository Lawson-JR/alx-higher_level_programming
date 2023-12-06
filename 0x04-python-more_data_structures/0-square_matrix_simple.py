#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        rows = [num ** 2 for num in row]
        new_matrix.append(rows)
    return new_matrix
