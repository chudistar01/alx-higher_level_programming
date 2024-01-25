#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_list = []
    for row in matrix:
        result = list(map(lambda x: x**2, row))
        new_list.append(result)
    return new_list
