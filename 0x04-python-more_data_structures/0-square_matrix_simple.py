#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_list = [x*x for x in row]
        new_matrix.append(new_list)
    return new_matrix
